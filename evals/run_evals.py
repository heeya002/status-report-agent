#!/usr/bin/env python3
"""Eval runner for the status-report-agent golden set.

For each case in evals/cases/:
  1. Runs the agent in eval mode (non-interactive; CLARIFY outputs stop
     instead of waiting for a human) via `claude -p`.
  2. Runs the judge over the agent output + rubric + per-case
     expectations, expecting strict JSON with binary hard gates.
  3. Derives PASS/FAIL in code: a case passes iff every gate passes.
     Quality scores (1-5) are informational.

Results land in evals/results/run-<timestamp>/ as per-case artifacts plus
results.md, and a summary table prints to the console. Exit code is
non-zero if any case fails.

Usage:
  python3 evals/run_evals.py                     # run all 15 cases
  python3 evals/run_evals.py --cases 07,13       # substring filter
  python3 evals/run_evals.py --reuse results/run-20260705-101500
                                                 # re-judge saved agent outputs
  python3 evals/run_evals.py --agent-model claude-sonnet-5 \
                             --judge-model claude-opus-4-8

Requires the `claude` CLI on PATH (stdlib-only otherwise).
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

EVALS_DIR = Path(__file__).resolve().parent
REPO_DIR = EVALS_DIR.parent
CASES_DIR = EVALS_DIR / "cases"
RESULTS_DIR = EVALS_DIR / "results"
AGENT_PROMPT_PATH = EVALS_DIR / "prompts" / "run-agent-eval.md"
JUDGE_PROMPT_PATH = EVALS_DIR / "judge" / "judge-prompt.md"
RUBRIC_PATH = REPO_DIR / "rubric.md"

GATE_KEYS = [
    "correct_mode",
    "clarify_no_draft",
    "clarify_targets",
    "required_sections",
    "severity_tags",
    "word_count",
    "must_include",
    "must_exclude",
    "no_invention",
]

QUALITY_KEYS = ["coverage", "structure", "tone", "conciseness"]


def run_claude(prompt: str, model: str | None, timeout: int = 600) -> str:
    cmd = ["claude", "-p", "--output-format", "text"]
    if model:
        cmd += ["--model", model]
    proc = subprocess.run(
        cmd, input=prompt, capture_output=True, text=True, timeout=timeout
    )
    if proc.returncode != 0:
        detail = (proc.stderr.strip() or proc.stdout.strip())[:500]
        raise RuntimeError(f"claude exited {proc.returncode}: {detail}")
    return proc.stdout.strip()


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                meta[key.strip()] = val.strip()
    return meta


def observed_mode(agent_output: str) -> str:
    first_line = agent_output.strip().splitlines()[0].strip() if agent_output.strip() else ""
    if first_line == "MODE: DRAFT":
        return "draft"
    if first_line == "MODE: CLARIFY":
        return "clarify"
    return "other"


def draft_word_count(agent_output: str) -> int:
    lines = agent_output.strip().splitlines()
    body = "\n".join(lines[1:]) if lines and lines[0].startswith("MODE:") else agent_output
    return len(re.findall(r"\S+", body))


def extract_json(text: str) -> dict:
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    start, end = text.find("{"), text.rfind("}")
    if start == -1 or end <= start:
        raise ValueError("no JSON object found in judge output")
    return json.loads(text[start : end + 1])


def build_agent_prompt(rubric: str, notes: str) -> str:
    return (
        f"{AGENT_PROMPT_PATH.read_text()}\n\n"
        f"=== RUBRIC (rubric.md) ===\n\n{rubric}\n\n"
        f"=== WEEKLY NOTES (input) ===\n\n{notes}\n"
    )


def build_judge_prompt(rubric: str, expectations: str, notes: str, agent_output: str) -> str:
    mode = observed_mode(agent_output)
    facts = f"HARNESS_OBSERVED_MODE: {mode}"
    if mode == "draft":
        facts += f"\nHARNESS_COMPUTED_WORD_COUNT: {draft_word_count(agent_output)}"
    return (
        f"{JUDGE_PROMPT_PATH.read_text()}\n\n"
        f"=== RUBRIC (rubric.md) ===\n\n{rubric}\n\n"
        f"=== CASE EXPECTATIONS ===\n\n{expectations}\n\n"
        f"=== INPUT NOTES (what the agent received) ===\n\n{notes}\n\n"
        f"=== HARNESS COMPUTED FACTS ===\n\n{facts}\n\n"
        f"=== AGENT OUTPUT UNDER EVALUATION ===\n\n{agent_output}\n"
    )


def judge_with_retry(prompt: str, model: str | None) -> dict:
    raw = run_claude(prompt, model)
    try:
        return extract_json(raw)
    except (ValueError, json.JSONDecodeError):
        raw = run_claude(
            prompt + "\n\nREMINDER: respond with ONLY the JSON object, nothing else.",
            model,
        )
        return extract_json(raw)


def evaluate_case(case_dir: Path, run_dir: Path, args, rubric: str) -> dict:
    case_id = case_dir.name
    notes = (case_dir / "input.md").read_text()
    expectations = (case_dir / "expectations.md").read_text()
    meta = parse_frontmatter(expectations)
    case_out_dir = run_dir / case_id
    case_out_dir.mkdir(parents=True, exist_ok=True)

    agent_output_path = case_out_dir / "agent-output.md"
    if args.reuse:
        reuse_path = EVALS_DIR / args.reuse / case_id / "agent-output.md"
        if not reuse_path.exists():
            raise FileNotFoundError(f"--reuse: no agent output at {reuse_path}")
        agent_output = reuse_path.read_text()
    else:
        agent_output = run_claude(build_agent_prompt(rubric, notes), args.agent_model)
    agent_output_path.write_text(agent_output)

    verdict_data = judge_with_retry(
        build_judge_prompt(rubric, expectations, notes, agent_output), args.judge_model
    )
    (case_out_dir / "judge.json").write_text(json.dumps(verdict_data, indent=2))

    gates = verdict_data.get("gates", {})
    failed = [
        k for k in GATE_KEYS if not gates.get(k, {}).get("pass", False)
    ]
    quality = verdict_data.get("quality", {})
    scores = [quality.get(k) for k in QUALITY_KEYS if isinstance(quality.get(k), (int, float))]
    quality_avg = round(sum(scores) / len(scores), 2) if scores else None

    return {
        "case_id": case_id,
        "category": meta.get("category", "?"),
        "expected_mode": meta.get("expected_mode", "?"),
        "observed_mode": verdict_data.get("observed_mode", observed_mode(agent_output)),
        "gates_passed": len(GATE_KEYS) - len(failed),
        "gates_total": len(GATE_KEYS),
        "failed_gates": failed,
        "quality_avg": quality_avg,
        "verdict": "PASS" if not failed else "FAIL",
        "notes": verdict_data.get("notes", ""),
    }


def format_table(rows: list[dict]) -> str:
    header = (
        "| Case | Category | Expected | Observed | Gates | Failed gates | Quality | Verdict |\n"
        "|------|----------|----------|----------|-------|--------------|---------|---------|\n"
    )
    lines = []
    for r in rows:
        failed = ", ".join(r["failed_gates"]) if r["failed_gates"] else "—"
        quality = f"{r['quality_avg']:.2f}" if r["quality_avg"] is not None else "—"
        lines.append(
            f"| {r['case_id']} | {r['category']} | {r['expected_mode']} "
            f"| {r['observed_mode']} | {r['gates_passed']}/{r['gates_total']} "
            f"| {failed} | {quality} | {r['verdict']} |"
        )
    return header + "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--cases", help="comma-separated substrings to filter case dirs")
    parser.add_argument("--agent-model", help="model for the agent run (default: CLI default)")
    parser.add_argument("--judge-model", help="model for the judge run (default: CLI default)")
    parser.add_argument(
        "--reuse",
        help="path relative to evals/ of a previous run dir; re-judges its saved agent outputs",
    )
    args = parser.parse_args()

    case_dirs = sorted(d for d in CASES_DIR.iterdir() if (d / "input.md").exists())
    if args.cases:
        wanted = [s.strip() for s in args.cases.split(",") if s.strip()]
        case_dirs = [d for d in case_dirs if any(w in d.name for w in wanted)]
    if not case_dirs:
        print("No cases matched.", file=sys.stderr)
        return 2

    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = RESULTS_DIR / f"run-{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)
    rubric = RUBRIC_PATH.read_text()

    rows = []
    for case_dir in case_dirs:
        print(f"[{case_dir.name}] running...", flush=True)
        try:
            row = evaluate_case(case_dir, run_dir, args, rubric)
        except Exception as exc:  # noqa: BLE001 - record and keep going
            row = {
                "case_id": case_dir.name,
                "category": "?",
                "expected_mode": "?",
                "observed_mode": "error",
                "gates_passed": 0,
                "gates_total": len(GATE_KEYS),
                "failed_gates": [f"harness_error: {exc}"],
                "quality_avg": None,
                "verdict": "ERROR",
                "notes": str(exc),
            }
        print(f"[{row['case_id']}] {row['verdict']}"
              + (f" — failed: {', '.join(row['failed_gates'])}" if row["failed_gates"] else ""))
        rows.append(row)

    table = format_table(rows)
    passed = sum(1 for r in rows if r["verdict"] == "PASS")
    summary = f"\n**{passed}/{len(rows)} cases passed.**\n"
    (run_dir / "results.md").write_text(
        f"# Eval results — {timestamp}\n\n"
        f"Agent model: {args.agent_model or 'CLI default'} · "
        f"Judge model: {args.judge_model or 'CLI default'}"
        + (f" · Reused agent outputs from {args.reuse}" if args.reuse else "")
        + f"\n\n{table}{summary}"
    )

    print()
    print(table)
    print(f"{passed}/{len(rows)} cases passed. Artifacts: {run_dir.relative_to(REPO_DIR)}")
    return 0 if passed == len(rows) else 1


if __name__ == "__main__":
    sys.exit(main())
