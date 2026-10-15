# Sections guide

Discussion prompts for each file in [SKILL.md](SKILL.md) step 4. One question at a time. Offer options and a recommendation for each. Ground the options in what the user already said.

## local-docs/goal.md

Private. Say so first. Then:

- **Goals**: What do they want out of this project for themselves, beyond the product? Push each toward something they could tell whether they achieved.
- **Learning targets**: For each skill, tool or plugin: where are they now, where do they want to be, and where in the project does it show up? Ask whether any stack choice should be made partly to learn something.
- **How to help**: How should the agent explain, when should it show versus do, and what should it point them to?
- **Boundaries**: What must the agent not do for them, because doing it is the point?
- **How they will know**: A concrete sign the goal was met.
- **Cleared for public files**: Go through the items that could direct an agent (teaching style, tools to prefer, reasons for choices). For each, propose neutral, agent-directed wording and ask whether it may go in a committed file. Anything they hesitate on stays private.

## context/PROJECT.md

- **Overview**: What does it do, who is it for, what problem does it solve? Draft one paragraph from their answer and confirm it.
- **Goals**: Which two or three outcomes would make this a success? Push each toward specific and measurable.
- **Core user flow**: Walk the path from first visit to the main value, one step at a time.
- **Features**: Group by category. Which are essential to the first version?
- **Scope**: What is explicitly in scope and what is explicitly out? Ask what they are tempted to build that should wait.
- **Success criteria**: Which verifiable conditions prove it works (for example "a signed-in user can create and open a project")?

## context/ARCHITECTURE.md

- **Stack**: Layer by layer (framework, UI, auth, database, other). Suggest options with trade-offs, recommend one, and record the reason. Include an option that fits a learning target from `goal.md`, and say it matches.
- **System boundaries**: Which folders exist and what does each own? Ask what must never live in each.
- **Storage model**: What lives in the database and what in file or blob storage?
- **Auth and access**: How do users sign in, what does ownership mean, who can change what?
- **Invariants**: Which rules must never be broken? Prompt with failure stories: "what would hurt most if the agent got it wrong?" Each gets a reason.

## context/UI-CONTEXT.md

- **Theme**: Dark, light, or both? Which existing products do they like the look of?
- **Colors**: Ask for the accent first, then derive the base, surface, text, border and state tokens and propose the hex values.
- **Typography**: UI font and mono font.
- **Border radius**: Scale per context (inline, cards, modals).
- **Component library**: Which library, where do components live, how are new ones added?
- **Layout patterns**: The two or three screens that set the pattern for the rest.
- **Icons**: Library, stroke style, sizes.

Skip this file when the project has no UI. Note that in the file's title section and in `DECISIONS.md`.

## context/CODING-STANDARDS.md

- **General**: Their three strongest coding principles.
- **Language**: Strictness, handling of `any`, validation of external input.
- **Framework**: Conventions for the chosen framework, from the stack decision.
- **Styling, API routes, data and storage**: Rules that follow from the architecture. Draft them from ARCHITECTURE.md and let the user amend.
- **File organization**: One line per folder, matching the system boundaries.

## context/AI-WORKFLOW-RULES.md

- **Approach**: How they want the agent to work (spec-driven, increments, review points).
- **Working with the user**: Draft from the approved rows in `goal.md`'s "Cleared for Public Files" and add anything else the user wants agents to do. Wording is public, so it stays free of personal detail.
- **When to split work**: The three concerns that should never share a step in this project.
- **Protected files**: Generated or third-party files the agent must not edit.
- **Keeping docs in sync**: Which docs must change when which things change.
- The WIP limit of 1 is part of the template. Keep it, and confirm the user is happy with it.

## AGENTS.md

- **Project overview**: Two sentences from PROJECT.md.
- **Tech stack and versions**: From ARCHITECTURE.md. Ask for exact versions.
- **First-run commands**: The real commands, in order.
- **Hard constraints**: Five to six non-negotiables. Draft from the invariants and the protected files, and ask what to add.
- Keep the docs map current, without `local-docs/` entries.

## Makefile

- Ask which lint, type-check, test and build commands exist yet. Chain them in `check`, and leave a check out only if the tool is not installed yet, logging that in Open Questions. The target must exit non-zero on any failure.

## context/PROGRESS.md

- **Current phase and goal**: Usually "Not started" and the first unit.
- **Next Steps**: Take the build plan's units, in order, each with a checkable Done when. Ask the user to confirm each condition is something they could check themselves.
- Leave Done and In Progress empty, or keep the repo-scaffolded item if the project already runs.

## context/DECISIONS.md

- Fill from choices made during this discussion. Each has date, decision, reasoning, and what it supersedes (when relevant).

## context/specs/

**00-build-plan.md**: An ordered list of units. Help the user decompose the project:

- Dependencies first, then security before functionality, backend before frontend wiring, UI shells before real data.
- Install packages in the unit where they first unlock behavior.
- Validate the order: does everything a unit needs exist in an earlier unit? Merge adjacent units that never stand alone.

**First spec** (`01-name.md`), with five sections:

- **Goal**: One or two concrete sentences.
- **Design**: Layout and tokens from `UI-CONTEXT.md`.
- **Implementation**: One sub-section per component or boundary.
- **Dependencies**: Packages this unit adds.
- **Verify when done**: A checklist of conditions.

Ask whether to write further specs now or generate each just before its unit is built. Recommend just before.

## local-docs/setup.md

- Prerequisites and versions, accounts and services, environment variables (name, where to get it, format), database setup, run and verify commands, deployment target, known troubleshooting. Draft from AGENTS.md and ARCHITECTURE.md, and ask about the gaps. Defer deployment when it is undecided.

## local-docs/architecture.html

- Draft from ARCHITECTURE.md and the decisions log: overview, system diagram, key flows, storage and data model, invariants with reasons.
- Give **every package, plugin, tool and external service** its own entry with what it does, why it was chosen, alternatives rejected, where it is used, and constraints. Take the list from the stack decisions, then ask what else they know they will use. Dependencies not chosen yet get added when they are.
