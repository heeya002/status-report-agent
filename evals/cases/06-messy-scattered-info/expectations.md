---
case_id: 06-messy-scattered-info
category: messy-complete
expected_mode: draft
---

# Expectations — 06: One blocker scattered across four fragments

The key blocker (site 44 export failure) is described in four separate
fragments: the failure (Monday), the cause (Wednesday), the impact
(midweek), and the deadline/escalation path (Friday). A correct draft
synthesizes all four into one coherent HIGH blocker bullet — the
information is complete, just scattered.

## Expected clarifying question topics

None — a CLARIFY response fails `correct_mode`.

## Must include

- Site 44 blocker tagged **[HIGH]**, synthesized: permissions misconfig
  blocks ~1,900 regulated records, cleanup fully stopped, IT fix ETA
  May 22 (already slipped twice), site drops to Wave 5 if the QA window
  is missed, escalation to IT lead if not fixed by Thursday
- Site 41 resolved: stays in Wave 4, new owner J. Osei, onboarding May 26
- COREMAP QA writeup submitted
- Priya staffing request submitted with KM lead endorsement, ops decision
  expected by June 5

## Must exclude

- Office hours attendance (input explicitly marks it "nothing worth
  reporting" — including it is noise)

## Judge notes

- The core test: the site 44 bullet must connect cause, scale (1,900
  regulated files), consequence (site slips to Wave 5), and the
  escalation trigger. A bullet that only says "export job failed" misses
  the synthesis and should fail `must_include`.
- Bullet-length limits may force the site 44 story across two bullets;
  that is acceptable if the substance survives.

## Known limitation — mis-specified input (flagged 2026-07-19)

Repeated runs (5x, same prompt and input) pass 0/5. Root cause: "the
ask: escalate to the IT lead if it's not fixed by thursday" is written
in the Friday entry, in a note where every other date anchors to 5/22
— "thursday" is never pinned to a date, and it's unclear whether it
means the Thursday just passed or the following week's. Across five
runs the agent handles this differently every time: bails to
`MODE: CLARIFY` to ask which Thursday is meant, which fails
`correct_mode` (2x); conflates the Thursday trigger with the 5/22 date
into one fabricated deadline, which fails `no_invention` (1x); drops
the Thursday trigger from the draft entirely, which fails
`must_include` (1x); and once drafted the synthesis correctly but
missed severity tags on two Risk bullets, which fails `severity_tags`
and appears to be unrelated noise (1x).

This is being tracked as an input defect, not a rubric or prompt
defect, and `expected_mode` is deliberately left as `draft` rather than
recategorized to `clarify`: this case's entire design intent is testing
synthesis of one blocker scattered across four fragments, not testing
date disambiguation, and moving the goalpost to `clarify` would mask
the underlying input defect rather than fix it. The correct fix is
pinning "thursday" to an explicit date (e.g., "by 5/21") in a future
revision of this case's `input.md`, not changing what counts as a pass.
