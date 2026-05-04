# Status Report Agent

A small agentic workflow built with Claude Code that turns messy weekly project notes into executive-ready status updates. The project demonstrates how knowledge management and governance principles translate to agentic AI design — through rubrics that define quality, human-in-the-loop checkpoints that preserve accountability, and traceable reasoning that makes the agent's decisions auditable. It solves a real problem most project leads face: losing two productive hours of their week — split across Friday afternoon and Monday morning — to transforming raw notes into something polished enough to send to leadership.

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

A prompt produces output in a single shot: input goes in, response comes out, the work is done. An agent, in the sense the term is used in 2026, does something different — it makes decisions across multiple steps, evaluates its own work against criteria, and changes behavior based on what it finds.

This project meets that bar through four concrete behaviors:

**Multi-step reasoning over single-shot output.** The workflow runs four sequential steps (classify, clarify, draft, self-check) rather than producing a final draft in one pass. Each step has a defined input, a defined output, and a defined purpose. The reasoning between steps is what separates this from a clever prompt.

**Self-evaluation against a rubric.** After drafting, the agent reads its own output against the rubric (word count, severity tags, section order, anti-patterns) and revises before returning. A prompt produces text and stops. This agent grades itself.

**Confidence-aware decision-making.** When the agent assigns severity tags, it distinguishes between calls grounded in explicit input ("blocked 10 days, will push next batch" → clearly HIGH) and calls inferred from softer urgency signals ("might need 2 more weeks" → inferred MEDIUM). It surfaces the inferred ones to the human for verification. Most agent demos don't track the difference between what they know and what they're guessing.

**Targeted human-in-the-loop checkpoints.** When input is genuinely ambiguous — vague sentiment, missing context, unclear severity — the agent pauses and asks a focused question rather than producing its best guess. This is a design constraint layered on top of agentic capability, not a replacement for it. The agent could guess; it's been instructed not to.

The result is an agent that reads, decides, evaluates, and asks — and stops short of executing on the human's behalf. That last boundary is deliberate, and the next section explains why.

---

## Design decisions

This section captures the judgment calls behind the agent. They reflect my background in knowledge operations, governance, and AI enablement in regulated environments — and they're the reason this project behaves the way it does.

### Human-in-the-loop by design

The agent never operates without a human in three specific places: the human provides the input notes, the human answers any clarifying questions the agent raises, and the human reviews the final draft before sending. The agent never auto-sends, never escalates on its own, and never assumes silence is consent.

This isn't a default I inherited; it's a deliberate constraint. In large-scale content migrations, automation can move and classify files quickly, but a human still has to confirm record types, access controls, retention rules, and legal hold exceptions — because the cost of a wrong call is compliance exposure, not just inconvenience. The same principle applies whenever AI-generated content touches regulated workflows: the agent can support, but qualified humans have to validate. This agent is built to that standard.

### Rubric-driven behavior

The agent's quality criteria live in `rubric.md` — a plain markdown file that defines required sections, format rules, severity tags, and classification logic. The agent reads the rubric at runtime. The code itself contains no judgment about what a "good" status update looks like; that judgment is fully externalized.

This separation is intentional. It means the people who actually understand the work — PMs, operations leads, domain experts — can edit how the agent behaves without touching code. Quality governance stays where it belongs: with the people accountable for it.

### Output to a local file, not auto-sent

When the agent finishes drafting, it writes the output to a local markdown file. The human opens the file, reviews it, edits anything that needs editing, and decides where it goes. The agent does not write to email, Slack, a Google Doc, or any other delivery surface.

This is a deliberate low-tech choice. Auto-send pipelines look impressive in demos, but they introduce risk that has nothing to do with the agent's actual job: bad output reaches its audience faster. Keeping the human in the delivery path is what makes the agent safe to use on real executive-facing content.

### Clarification is a governance feature

When input is genuinely ambiguous — a vague sentiment ("they seem happy"), a missing detail (no severity signal), a piece of context the agent can't infer — the agent stops and asks the human a focused question rather than guessing.

This is often described as a usability feature. It's actually a governance feature. Hallucination doesn't happen because models are careless; it happens because they're trained to produce plausible output regardless of input quality. The clarify step interrupts that default. By forcing the agent to ask, the project keeps accountability for content quality with the human, where it belongs.

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
