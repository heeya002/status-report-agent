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

This is a Claude Code project. You run the agent by pasting a prompt into a Claude Code session, then telling it which input file to use. The agent reads your notes, asks clarifying questions, drafts a status report, self-checks against the rubric, and writes the final draft to a file for your review.

### Prerequisites

- [Claude Code](https://code.claude.com/docs/en/overview) installed
- [Git](https://git-scm.com/downloads) installed (for cloning the repo)
- An Anthropic API key configured for Claude Code
- A terminal application (Terminal on macOS, any equivalent on Linux/Windows)

### 1. Clone the repo

In your terminal application, run:

```bash
git clone https://github.com/heeya002/status-report-agent.git
cd status-report-agent
```

### 2. Start Claude Code in the project folder

```bash
claude
```

This opens a Claude Code session inside the project. The agent needs to be inside this folder so it can read `rubric.md`, your input file, and write to `outputs/`.

### 3. Run the demo

Copy the entire contents of `prompts/run-agent.md` and paste it into Claude Code. On a new line at the end of your paste, add:

```
Run this on samples/sample-2-blocked-week.md.
```

Press Enter. The agent will:

1. Read the rubric and the input file
2. Classify each item in the notes
3. Ask you a numbered list of clarifying questions where the input is ambiguous (severity unclear, missing context, unclear next steps, ambiguous sentiment)
4. Wait for your answers
5. Draft the status report against the rubric
6. Self-check the draft and revise if needed
7. Write the final draft to `outputs/status-report-{today's-date}.md`

A complete run takes a few minutes including the time to answer clarifying questions.

### 4. Run it on your own notes

Drop your weekly notes as a `.md` file into the `inputs/` folder. Then start a Claude Code session and paste the same prompt, but point at your file:

```
Run this on inputs/my-notes-2026-05-10.md.
```

The samples in `samples/` stay untouched — they're reference examples showing what good input looks like.

The agent writes your draft to `outputs/status-report-{today's-date}.md` (for example, `outputs/status-report-2026-05-11.md`). Open the file in any text editor to review.

### 5. See an example output

`outputs/example-output-sample-2.md` is a real draft the agent produced from `samples/sample-2-blocked-week.md`. It shows what the four sections look like (This Week's Progress, Risks and Blockers, Decisions Needed, Next Week's Focus), how severity tags appear inline, and how the rubric's word-count and bullet-count constraints shape the output.

---

## Project structure

```
status-report-agent/
├── README.md                          ← This file
├── rubric.md                          ← Quality rubric the agent grades itself against
├── prompts/
│   └── run-agent.md                   ← The prompt that runs the four-step workflow
├── samples/                           ← Demo input files showing what good input looks like
│   ├── sample-1-clean-week.md
│   ├── sample-2-blocked-week.md
│   └── sample-3-decision-pending.md
├── inputs/                            ← Where you put your own weekly notes
└── outputs/                           ← Where the agent writes drafted status reports
    └── example-output-sample-2.md     ← A real draft from sample-2 (see Section 6)
```

Two things to notice about how the project is laid out:

**Business logic lives outside code.** The rubric and the run prompt are plain markdown files, not buried inside a script. A PM, ops lead, or domain expert can open `rubric.md` and tune the quality criteria — word counts, severity rules, anti-patterns — without touching engineering. Same for `prompts/run-agent.md`. This is deliberate: the people closest to the work should be able to shape how the agent behaves.

**Source material and generated material stay separated.** `samples/` holds reference examples that ship with the repo and shouldn't be modified. `inputs/` is where users drop their own notes. `outputs/` is where drafts land. A user always knows what's theirs, what the agent produced, and what came with the project.

---

## Production extensions

The agent writes to a local file by design, not as a limitation. Local output preserves the human-review checkpoint (the draft can't auto-send), avoids OAuth and credential setup that would slow down a portfolio demo, and stays portable across teams who use different downstream tools.

In a production deployment, several extensions would make sense — each one preserving the human-review checkpoint rather than removing it.

**Google Doc or SharePoint integration.** Instead of writing to a local `.md` file, the agent writes the draft into a shared Doc or SharePoint location with the ops lead as the owner. The owner reviews, edits, and decides where to send it. IT and the document platform owner partner on the integration; lifecycle and retention policies are inherited from the platform's existing governance.

**Slack approval bot.** After self-check passes, the agent posts the draft into a private Slack channel where the ops lead and one or two reviewers can approve, request changes, or escalate. The bot does not send anywhere until a human clicks "approve." This adds a second human checkpoint without removing the first.

**Email-to-self.** The agent sends the draft to the ops lead's own inbox as a working draft. The lead reviews, edits in their email client, and forwards to leadership when ready. Lowest-friction option; useful for teams without a shared workspace.

**Tracker integration (Airtable, Notion, Jira).** Each item the agent classifies — Progress, Blocker, Decision Needed, Risk — flows into the team's existing tracker as a record with the severity tag attached. This keeps the status report in sync with the team's working data instead of being a one-off document. Ops owns the tracker schema; the agent populates it.

**Multi-team rollout.** A single rubric works for one team. For multi-team deployment, each team forks the rubric to reflect their own quality criteria (different severity rules, different required sections, different anti-patterns). Central ops owns a baseline rubric; team leads maintain their own variants. The prompt stays shared; only the rubric varies.

In every case, the human-review checkpoint stays. The agent drafts; a person decides what to do with the draft. That boundary is what makes the system safe to deploy at scale.

---

## What this project is not

This is a portfolio project demonstrating a design pattern for agentic workflows with human-in-the-loop guardrails. It is not:

**A production system.** The agent runs locally in a Claude Code session against a single user's notes. There is no shared deployment, no authentication, no audit logging, no usage telemetry. A real production version would require all of those, scoped by IT and legal before rollout.

**A replacement for existing status reporting tools.** Teams that already have a working status report process — a template, a meeting cadence, a tracker — don't need this. The agent is most useful for teams whose notes are messy, whose status reports are inconsistent, or whose ops leads are drowning in synthesis work.

**A general-purpose AI agent framework.** The four-step workflow (Classify → Clarify → Draft → Self-check) is designed for one specific task: turning weekly project notes into a status report. The same pattern could be adapted to other drafting tasks (meeting summaries, incident postmortems, customer escalation reviews), but each adaptation would need its own rubric, its own clarification logic, and its own validation against real users.

**A finished product.** The rubric is opinionated and reflects my own judgment from operations experience. In a real deployment, it would be co-designed with stakeholders and validated against historical examples. The clarification questions reflect the categories I considered most material; another ops lead might prioritize differently. These are starting points, not final answers.

What this project *is*: a working demonstration of how an AI drafting assistant can be built with governance baked in from the start, rather than retrofitted onto an autonomous system. The pattern is real. The implementation is a demo.

---

## About this project

I'm Sunny Kim, co-founder of [Realatable](https://www.realatable.io/), an AI enablement venture focused on practical, governed AI workflows for operations teams.

I built this project to demonstrate a specific pattern: how to design an AI drafting assistant with governance baked in from the start, rather than retrofitted onto an autonomous system. The four-step workflow, the human-in-the-loop checkpoints, the rubric-as-editable-file, the local output for human review — these aren't features I added because they sounded good. They reflect a decade of operations and knowledge management work in regulated environments, where I learned that AI tools succeed or fail based on whether the people closest to the work can shape and trust them.

This is a portfolio project, not a product. The repo is open for anyone who wants to read the design, fork the pattern, or critique the choices. If any of it is useful to you — as a reference, a starting point, or a counter-example — I'd like to hear about it.

**Links**

- Repo: [github.com/heeya002/status-report-agent](https://github.com/heeya002/status-report-agent)
- LinkedIn: [linkedin.com/in/sunny-kim-a4b17b55](https://www.linkedin.com/in/sunny-kim-a4b17b55/)
- Realatable: [realatable.io](https://www.realatable.io/)
