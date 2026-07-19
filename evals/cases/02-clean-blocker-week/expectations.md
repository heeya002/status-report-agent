---
case_id: 02-clean-blocker-week
category: clean-complete
expected_mode: draft
---

# Expectations — 02: Clean week with explicit blocker, no decisions

Clean input where severities are stated explicitly and the Decisions
section is explicitly empty. Tests severity pass-through and the rubric's
"None this week." rule for empty sections.

## Expected clarifying question topics

None — a CLARIFY response fails `correct_mode`.

## Must include

- Clinical Ops batch progress: 4,200 of ~11,000 files migrated
- COREMAP confirmed the QA approach meets records requirements
- Site 9 legal hold blocker tagged **[HIGH]**: pending 11 days, 2,700
  files frozen, blocks Clinical Ops part 2, needs e-Discovery escalation
- Storage capacity risk tagged **[MEDIUM]**: 82% capacity, full by early
  June forecast
- Decisions Needed section present with "None this week." (or equivalent)

## Must exclude

- Nothing case-specific. Standard rubric anti-patterns apply.

## Judge notes

- Skipping the Decisions Needed section entirely fails
  `required_sections`; it must appear with a "None this week." note.
- Severities are explicit in the input; any re-rating fails
  `severity_tags`.
