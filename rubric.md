# Status Report Rubric

This rubric defines what a good weekly executive status update looks like.
It reflects my judgment based on 10+ years of operations and knowledge
management experience in regulated environments. In production, this
rubric would be co-designed with stakeholders (executives, team leads,
PMO) and validated against historical examples.

The agent reads this file at runtime. To change how the agent behaves,
edit this file — no code changes required.

---
## Audience

The status update is written for the user's direct manager, the KM Team
Lead, who is part of ECD leadership. The reader is a KM expert who
understands the work context, skims quickly between meetings, and cares
most about progress milestones, risks that threaten delivery, decisions
that need to be escalated, and items requiring their input or endorsement.

The update may be forwarded upward to ECD leadership (VP / Senior Director
level), so it should read cleanly without the reader needing to add
context.

## 1. Required sections and order

Every status update must contain these four sections, in this exact order:

1. **This Week's Progress** — concrete accomplishments that moved work forward
2. **Risks and Blockers** — items that could delay or derail work, with severity
3. **Decisions Needed** — specific items requiring input from the reader
4. **Next Week's Focus** — top 2–3 priorities for the coming week

If a section has no content for a given week, include the section heading
with the note "None this week." Do not skip sections. Consistency of
structure helps executive readers skim efficiently.

## 2. Format and length rules

- **Total length**: Under 300 words. Target 200.
- **Format**: Markdown, with section headings using `##` and bullet lists
  using `-`.
- **Bullets per section**: 2–5 bullets. Never exceed 5. If more than 5
  items exist, combine or escalate the least critical to a "for awareness"
  note.
- **Bullet length**: Under 25 words per bullet. One sentence maximum.
- **No paragraphs**: Executive readers scan bullets, not paragraphs.
  Convert any paragraph-style content into bullets.
- **No preamble**: Do not start with "Hi team" or "This week has been
  productive." Start directly with the first section heading.

## 3. Tone and language rules

- **Specific over vague**: Numbers, names, and dates over general claims.
  "Completed user testing with 8 participants" not "Did some user testing."
- **Active voice**: "The team delivered X" not "X was delivered by the team."
- **Factual over promotional**: State what happened. Avoid adjectives like
  "exciting," "great," "amazing." Executives find these hollow.
- **No hedging language**: Avoid "I think," "probably," "hopefully,"
  "might." If the information is uncertain, flag the uncertainty
  explicitly: "Timing unconfirmed — awaiting vendor response."
- **No jargon without context**: Acronyms must be spelled out on first use
  unless they are universally known within the organization.

## 4. Severity rating for risks and blockers

Every item in the "Risks and Blockers" section must be tagged with a
severity level:

- **[HIGH]** — Active blocker; work cannot proceed; requires action this week
- **[MEDIUM]** — Emerging risk; work can proceed but outcome is uncertain
  without intervention; requires decision or support within 2 weeks
- **[LOW]** — Known issue being monitored; no action needed from the reader

Format example:
- **[HIGH]** Legal review of vendor contract pending for 10 days; blocks
  Phase 2 kickoff. Need escalation to Legal lead by Wednesday.

If the input does not clearly indicate severity, the agent must ask the
user before assigning one. The agent must not guess severity.

## 5. Anti-patterns (never do these)

The agent must avoid all of the following:

- **Do not invent details.** If input is vague, ask the user to clarify
  rather than fill in plausible-sounding specifics.
- **Do not soften blockers.** If something is blocked, say so clearly.
  Do not write "progressing with some challenges" when the reality is
  "blocked until Legal responds."
- **Do not include internal team-only content.** Inside jokes, Slack
  reactions, tangential discussion, and personal updates are noise for
  executive readers. Filter these out.
- **Do not auto-send or auto-post.** Output must be written to a local
  file for human review. The user decides when and where to send the
  final version.
- **Do not restate the input verbatim.** The agent's job is to synthesize
  and structure, not to reformat raw notes.

---

*Last updated: April 2026*
*Rubric designed by Sunny Kim (Realatable). Intended for portfolio
demonstration. In a real enterprise deployment, this rubric would be
iteratively refined with stakeholders and validated against historical
examples.*
