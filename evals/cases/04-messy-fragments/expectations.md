---
case_id: 04-messy-fragments
category: messy-complete
expected_mode: draft
---

# Expectations — 04: Unordered fragments with typos

Same information completeness as category 1, delivered as fragments with
typos ("meting", "signd"), inconsistent day markers, shouting, and "lol".
Every fact needed for a draft is present with explicit severity signals.
Messiness must not degrade output quality or trigger clarification.

## Expected clarifying question topics

None — a CLARIFY response fails `correct_mode`. Messiness is not
ambiguity.

## Must include

- Wave 4 scope confirmed: 5 sites, ~22k files; kickoff comms out
- COREMAP signed off the QA sampling doc
- Site 41 blocker tagged **[HIGH]**: 17 days no reply, prep fully stuck,
  dept-head contact needed this week or the site drops from Wave 4
- Vendor tool outage tagged **[LOW]** (explicit: monitoring only, no
  action needed, RCA due May 12)
- Decision: regulatory 3-month (revised from 6) deferral, KM Team Lead
  yes/no by May 15
- Site 44 owner engaged; onboarding call May 11

## Must exclude

- Informal register leaking through: "lol", "!!!", "notes to self" tone

## Judge notes

- The tone in the draft must be executive-clean even though the input is
  not; sloppy tone here scores low on `tone` but is not a gate failure
  unless excluded content leaks.
- The Priya/Kelly coverage note is internal team logistics — reasonable
  to drop as NOISE; its absence is not a `must_include` failure.

## Known limitation — mis-specified input (flagged 2026-07-19)

Repeated runs (5x, same prompt and input) pass only ~1/5 of the time.
Root cause: "the regulatory deferral from last month, they came back
asking for 3 months instead of 6" leaves "they" unresolved. Across runs
the agent resolves it three different ways: correctly (1x), by
fabricating an attribution to "vendor" — pattern-matched from the
unrelated vendor-outage note earlier in the same input — which fails
`no_invention` (2x), and by dropping an unrelated stated fact
("comms went out") which fails `must_include` (2x).

This is being tracked as an input defect, not a rubric or prompt defect,
and `expected_mode` is deliberately left as `draft` rather than
recategorized to `clarify`: this case's category (messy-complete) is
designed to test that messiness doesn't trigger unnecessary
clarification, and a competent human reader would resolve "they" as the
regulatory contact without hesitation — the ambiguity is an artifact of
underspecified phrasing, not a case that should genuinely block
drafting. The correct fix is tightening "they" to an explicit noun
(e.g., "the regulatory contact") in a future revision of this case's
`input.md`, not changing what counts as a pass.
