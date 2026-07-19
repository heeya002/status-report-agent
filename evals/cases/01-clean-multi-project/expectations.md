---
case_id: 01-clean-multi-project
category: clean-complete
expected_mode: draft
---

# Expectations — 01: Clean, complete, multi-project week

Baseline case. Notes are well organized and cover all three named
projects with explicit statuses, an explicitly signaled HIGH blocker, and
a clearly scoped decision. There is nothing to clarify: the agent should
draft directly and cover all three projects.

## Expected clarifying question topics

None — a CLARIFY response fails `correct_mode`.

## Must include

- Legal dept batch complete: 9,400 files, zero access-control exceptions
- Training platform license renewal blocker, tagged **[HIGH]** (explicit:
  active blocker, 8 days stuck, April 15 deadline, May sessions at stake)
- Wave 4 announcement sequencing decision for the KM Team Lead, by April 17
- Audit response on track for April 24
- Next week's focus includes Clinical Ops kickoff and the license escalation

## Must exclude

- Nothing case-specific. Standard rubric anti-patterns apply.

## Judge notes

- All three projects (Wave 3 migration, audit response, training refresh)
  must be represented in the draft — dropping one is a `must_include`
  failure.
- The license blocker has explicit severity signals; tagging it MEDIUM or
  LOW fails `severity_tags`.
