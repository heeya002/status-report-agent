---
case_id: 05-messy-mixed-formats
category: messy-complete
expected_mode: draft
---

# Expectations — 05: Mixed formats (email paste, Slack paste, TODO list)

Complete information scattered across a forwarded email, a pasted Slack
exchange, a TODO list, and loose prose. Everything needed to draft is
present; severity signals are explicit. Tests synthesis across formats.

## Expected clarifying question topics

None — a CLARIFY response fails `correct_mode`.

## Must include

- Storage expansion approved (40TB archive tier, no ECD budget impact) —
  April storage risk closed
- QA sampling round 1: 2 metadata mismatches in 800 records, both fixed,
  root cause patched
- Site 44 onboarding done; cleanup starts May 18
- Site 41 risk tagged **[MEDIUM]** or **[LOW]** (explicit: work proceeds,
  drop/keep decision after the May 19 meeting, awareness only)
- Priya contract-end staffing risk: coverage gap after June 30, staffing
  call needed within 2 weeks (tagged **[MEDIUM]** per explicit
  "within 2 weeks" signal)
- Regulatory deferral approved May 12 (progress — decision already made)

## Must exclude

- Raw Slack/email formatting artifacts ("dana:", "me:", "FW:", "[x]")
- The approved deferral appearing under Decisions Needed (it is resolved)

## Judge notes

- Site 41 is explicitly flagged as awareness-only with work proceeding;
  tagging it HIGH fails `severity_tags`.
- The Priya staffing call is arguably a decision for the KM lead; either
  Risks (MEDIUM) or Decisions Needed placement is acceptable, as long as
  the 2-week window and June 30 gap are stated.
