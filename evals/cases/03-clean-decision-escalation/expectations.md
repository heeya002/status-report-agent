---
case_id: 03-clean-decision-escalation
category: clean-complete
expected_mode: draft
---

# Expectations — 03: Clean week with two escalation decisions

Clean input with two genuine DECISION items (both require the KM Team
Lead per the rubric's DECISION rule) and one explicit MEDIUM risk. Tests
that real escalations land in Decisions Needed, not Risks.

## Expected clarifying question topics

None — a CLARIFY response fails `correct_mode`.

## Must include

- Clinical Ops part 1 complete: 11,000 files, 14 access exceptions resolved
- Site 9 legal hold cleared after escalation
- Sites 41/44 non-response risk tagged **[MEDIUM]** with the April 29
  slip condition
- Decision 1: regulatory affairs 6-month Wave 4 deferral (~18,000 files,
  decision by May 1)
- Decision 2: legacy My Drive search index decommission — confirm no ECD
  retention dependency

## Must exclude

- Nothing case-specific. Standard rubric anti-patterns apply.

## Judge notes

- Both decisions must appear under Decisions Needed. Filing either as a
  risk (or dropping one) fails `must_include`.
- The Sites 41/44 item is explicitly a proceed-with-uncertainty risk;
  tagging it HIGH fails `severity_tags`.
