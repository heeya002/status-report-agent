# Status Report Agent

A small agentic workflow built with Claude Code that turns messy weekly project notes into executive-ready status updates. The project demonstrates how knowledge management and governance principles translate to agentic AI design — through rubrics that define quality, human-in-the-loop checkpoints that preserve accountability, and traceable reasoning that makes the agent's decisions auditable. It solves a real problem most project leads face: spending 45–90 minutes every Monday morning transforming raw notes into something polished enough to send to leadership.

---

## Why this exists

Team leads and project managers do the same quiet ritual every week: they start drafting a status update on Friday afternoon when they're trying to wrap up the week, and they finish it on Monday morning when they're trying to start a new one. The drafting isn't hard, exactly — but it pulls focus across the worst possible hours of the week, when everything else is either ending or beginning.

The work is mostly mechanical: gathering scattered notes, pasted Slack threads, and meeting fragments; deciding what's worth surfacing; flagging risks; calling out decisions the reader needs to make. A human can do all of this. They just lose two productive hours of their week to it, every week.

The Status Report Agent absorbs the mechanical part. It reads the messy weekly notes, classifies what matters, drafts the executive-ready update following a defined rubric, and asks for clarification when input is ambiguous. The human still owns the substance — what to escalate, how to frame a decision, when to send — but no longer has to own the formatting, the structuring, and the first-pass triage.

---

## What it does

The agent runs a four-step workflow against a single file of raw weekly notes:

**1. Classify.** It reads each line of the notes and tags it as PROGRESS, RISK, DECISION, or NOISE based on the rubric. Routine chatter and team-internal detail get dropped. Cross-functional touchpoints, blockers, and items requiring escalation get surfaced.

**2. Clarify.** When a note is genuinely ambiguous — vague sentiment, unclear severity, missing context — the agent asks the human a focused question rather than guessing. The human answers, and the agent continues. This step is what keeps the agent honest about its own limits.

**3. Draft.** Using the classified items, the agent writes a status update following the rubric: four required sections, severity tags on every risk, under 300 words, no preamble, no padding. The output matches the format an executive reader expects week to week.

**4. Self-check.** The agent reviews its own draft against the rubric and surfaces any judgment calls the human should verify before sending — for example, severity ratings inferred from urgency signals rather than explicit input, or items that were dropped to stay under the bullet cap.

The output is a markdown file the human reviews, edits, and sends. The agent never sends anything itself.

---

## Why it's agentic, not just a prompt

<TO FILL IN: explanation of what makes this agentic rather than a
one-shot prompt. Multi-step decision-making, self-checking against a
rubric, asking for human clarification when input is ambiguous. This
section is for readers who are evaluating technical depth.>

---

## Design decisions

This section captures the judgment calls behind the agent. These are the
design decisions that reflect my operations and knowledge management
background.

### Human-in-the-loop by design

<TO FILL IN: Human in 3 places - input stage (human provides notes),
clarify stage (agent asks human before proceeding on ambiguous items),
output stage (human reviews draft before sending; agent never
auto-sends). The agent is a drafting assistant with guardrails, not an
autonomous decision-maker.>

### Rubric-driven behavior

<TO FILL IN: The rubric file defines what "good" looks like and is the
source of truth for the agent's behavior. Reflects my judgment based on
operations experience. In a real enterprise deployment, the rubric would
be co-designed with stakeholders and validated against historical
examples. Note that the rubric is a plain markdown file, editable by
non-engineers - PMs, ops leads, domain experts - without code changes.>

### Output to a local file, not auto-sent

<TO FILL IN: The agent writes the final draft to a local markdown file.
The human reviews and decides when/where to send. This is a deliberate
low-tech choice for human control, portability (no OAuth setup), and
matching real user behavior - people want drafts they can tweak, not
auto-sent emails.>

### Clarification is a governance feature

<TO FILL IN: When input is ambiguous, the agent asks for clarification
rather than guessing. This prevents hallucination and forces human
accountability for the final content.>

---

## How to run it

<TO FILL IN: step-by-step instructions. Clone the repo, install Claude
Code, authenticate, run the agent against one of the samples. Should be
simple enough that a non-engineer could follow it.>

---

## Project structure

<TO FILL IN: brief description of each file and folder - rubric.md,
samples/, prompts/, main agent script, README. Explain why each piece
exists.>

---

## Production extensions

<TO FILL IN: a short list of how this demo would be extended for
production use - Google Doc output, Slack approval bot, email-to-self
for review, Airtable or Notion tracker. Signal that I understand the
full lifecycle, not just the demo.>

---

## What this project is not

<TO FILL IN: honest scope boundaries. Not a production system. Not
validated. Not autonomous. The rubric is my design, not co-designed
with real stakeholders. The samples are synthetic, based on real
project types I ran but not drawn from actual company data. These
honesty notes are a strength, not a weakness - they signal you know the
difference between a demo and production.>

---

## About this project

<TO FILL IN: one paragraph about you - your background in knowledge
operations, digital transformation, and AI enablement. Why this project
connects to your career direction. Link to your LinkedIn. Brief mention
of Realatable if relevant.>

---

*Built April 2026 by Sunny Kim. Feedback welcome.*
