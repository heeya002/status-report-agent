# Eval Plan — Status Report Agent

A golden-set eval harness for the status report agent. It tests the two
behaviors that matter most: **drafting quality** when input is complete
(however messy), and **knowing when to stop and ask** when it isn't —
plus the judgment traps (venting, confidential detail, blame) that are
this project's human-in-the-loop story in miniature.

---

## Structure

```
evals/
├── EVAL_PLAN.md              ← This file
├── prompts/
│   └── run-agent-eval.md     ← Eval-mode agent prompt (non-interactive)
├── judge/
│   └── judge-prompt.md       ← LLM judge: hard gates + quality scores, strict JSON
├── cases/                    ← 15 golden cases, one directory each
│   └── <case-id>/
│       ├── input.md          ← Raw weekly notes fed to the agent
│       └── expectations.md   ← What this case tests: expected mode,
│                               must-include facts, must-exclude content
├── run_evals.py              ← Runner: agent → judge → results table
└── results/                  ← Run artifacts (gitignored)
    └── run-<timestamp>/
        ├── <case-id>/
        │   ├── agent-output.md
        │   └── judge.json
        └── results.md
```

## Golden set (15 cases, 5 categories × 3)

| # | Category | Cases | What it tests | Expected behavior |
|---|----------|-------|---------------|-------------------|
| 1 | Clean & complete | 01–03 | Baseline — well-organized notes covering all projects | Draft directly, no clarification, all projects covered |
| 2 | Messy but complete | 04–06 | Unordered fragments, mixed formats, typos, info scattered | Same quality draft as category 1 — messiness must not degrade output |
| 3 | Ambiguous / incomplete | 07–09 | Missing status for a named project, unclear owner, vague blocker | Agent STOPS and asks the right clarifying question (tests the Clarify step) |
| 4 | Edge cases | 10–12 | (a) near-empty input, (b) contradictory statements, (c) huge rambling brain-dump | Graceful handling: ask for input / flag the contradiction / compress without losing key items |
| 5 | Judgment traps | 13–15 | Venting about a colleague, confidential salary detail, blame language | Draft must EXCLUDE inappropriate content — the HITL/guardrails story in miniature |

The cases share one continuous project world (the My Drive → Shared
Drive migration, COREMAP, e-Discovery, ECD leadership, Dana/Mark/Kelly)
so they read like real consecutive weeks from this repo's samples.

## Eval mode

`prompts/run-agent-eval.md` is the non-interactive variant of
`prompts/run-agent.md`. Same four-step workflow, one change: with no
human available, Step 2 emits its questions and stops instead of
waiting. Output contract:

- First line is exactly `MODE: DRAFT` or `MODE: CLARIFY`
- `DRAFT` → the status report only; `CLARIFY` → a numbered question list
  only, **no** draft or partial draft

This makes "did the agent stop and ask?" machine-checkable, and makes
drafting-when-it-should-have-asked an unambiguous failure.

## Judging

The judge (`judge/judge-prompt.md`) receives the rubric, the case's
`expectations.md`, the agent output, and two harness-computed facts
(observed mode and, for drafts, the word count — computed in code so the
judge never has to count). It returns **strict JSON only**:

- **9 binary hard gates** — mode correctness, clarify discipline,
  section order, severity tags, word count, must-include coverage,
  must-exclude leakage, no invented details. Gates that don't apply to a
  case's expected mode auto-pass as N/A.
- **4 quality scores (1–5)** — coverage, structure, tone, conciseness.
  Informational; they track drift (e.g., category 2 scoring below
  category 1 means messiness is degrading output) but don't gate.

The runner — not the judge — derives the verdict: **a case passes iff
every gate passes.** The judge reports evidence; the code does the
arithmetic.

## Running

```bash
python3 evals/run_evals.py                     # all 15 cases
python3 evals/run_evals.py --cases 07,13       # filter by substring
python3 evals/run_evals.py --reuse results/run-20260705-101500
                                               # re-judge saved outputs (iterate on the judge for free)
python3 evals/run_evals.py --agent-model claude-sonnet-5 --judge-model claude-opus-4-8
```

Requires the `claude` CLI on PATH; the runner is stdlib-only Python.
Each full run makes 30 model calls (agent + judge per case). Artifacts
land in `evals/results/run-<timestamp>/`; a markdown results table is
written there and printed to the console. Exit code is non-zero if any
case fails, so the run works as a CI gate.

## Editing and extending

- **Tune a case**: edit its `input.md` / `expectations.md` — both are
  plain markdown, consistent with this repo's business-logic-outside-code
  principle. `expectations.md` frontmatter (`expected_mode`) is the only
  machine-read field.
- **Add a case**: new directory under `cases/` with `input.md` +
  `expectations.md`. The runner discovers it automatically.
- **Tighten the judge**: edit `judge/judge-prompt.md`, then re-judge an
  existing run with `--reuse` — no agent calls needed.
- **Known limits**: single run per case (no variance measurement), and
  the judge is itself a model — spot-check `judge.json` evidence lines
  when a verdict looks off, especially early on.
