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
