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

## Known limitation — dual-classification gap (flagged 2026-07-19)

Passes only 1/3 runs. Both failures fail `must_include` the same way:
Site 41 gets classified as Progress only ("dept head responded, meeting
set for 5/19...") and drops out of Risks and Blockers entirely — no
severity tag anywhere.

Unlike `04-messy-fragments` and `06-messy-scattered-info`, this is not
an unresolved-reference problem — the input is unambiguous: "site 41:
dept head replied!! meeting set for 5/19. until that lands, site 41
stays out of wave 4 scope planning. drop/keep decision comes after the
meeting — nothing needed from the KM lead yet, just flagging so it's on
her radar. work proceeds on the other 4 sites meanwhile." That's one
item with genuine content on both sides: real Progress (dept head
replied, meeting scheduled) and real Risk/awareness (pending drop/keep
decision, explicitly asked to be flagged for the KM lead's radar). A
correct draft surfaces both. In 2 of 3 runs the agent collapses it into
Progress only and silently drops the Risk side.

This is a classification-discipline gap in Step 1 (an item can require
entries in more than one section, and the agent isn't consistently
doing that), not an input defect — there's nothing to tighten in
`input.md`. It's tracked separately from the 04/06 reference-resolution
issue and is not being fixed in this pass; a Step 1 rule requiring
dual-classified items to appear in every section they qualify for would
be the natural fix, out of scope here.
