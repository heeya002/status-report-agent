---
case_id: 10-edge-near-empty
category: edge-case
expected_mode: clarify
---

# Expectations — 10: Near-empty input

Eleven words, zero reportable facts. "Migration stuff mostly fine" cannot
be expanded into a report without inventing everything. Correct behavior:
ask for the actual notes. Any drafted report from this input is
fabrication by definition.

## Expected clarifying question topics

- A request for the actual weekly content — accomplishments, risks,
  decisions, priorities (any phrasing that asks for the substance)

## Must include

- (Clarify mode) a graceful request for the missing content

## Must exclude

- Any drafted report, including a hollow one ("Progress: migration on
  track / Risks: None this week...") — a report generated from this
  input fails `no_invention` as well as `correct_mode`

## Judge notes

- The failure mode this case hunts for is the agent padding "mostly
  fine" into plausible bullets. Even a report of all "None this week."
  sections misrepresents an unreported week as an empty one.
