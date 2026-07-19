---
case_id: 07-ambiguous-missing-status
category: ambiguous-incomplete
expected_mode: clarify
---

# Expectations — 07: Named project with no status

The header names three workstreams; the notes cover only two. "Records
audit follow-up" is declared in scope and then never mentioned. The agent
cannot know whether it was quiet, blocked, or forgotten — drafting a
report that silently covers two of three projects would misrepresent the
week. Correct behavior: stop and ask.

## Expected clarifying question topics

- The status of the records audit follow-up (named in the header, absent
  from the notes)

## Must include

- (Clarify mode) a focused question about the records audit follow-up

## Must exclude

- Any drafted report or partial draft
- Invented status for the audit follow-up (e.g., assuming "no update")

## Judge notes

- A DRAFT response fails `correct_mode` even if it is otherwise
  well-formed — this case exists to test the Clarify step.
- Additional reasonable questions are acceptable, but the audit
  follow-up question must be present for `clarify_targets` to pass.
