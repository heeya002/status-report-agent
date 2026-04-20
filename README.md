# Status Report Agent

A small agentic workflow built with Claude Code that turns messy weekly
project notes into executive-ready status updates.

<TO FILL IN: one-paragraph summary of what the agent does, who it's for,
and what makes it interesting. Written for a non-technical reader.>

---

## Why this exists

<TO FILL IN: the problem. Team leads and project managers spend 45-90
minutes every week transforming raw notes into polished status updates
for leadership. This agent does the first draft in 30 seconds. Frame
the reader's pain point first, then the agent as a response to it.>

---

## What it does

<TO FILL IN: plain-language description of the 4-step workflow -
classify, clarify, draft, self-check. Keep this short. Visual diagram
or screenshot would help here.>

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
