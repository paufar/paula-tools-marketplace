# AGENTS.md

Entry point for every coding agent session. Read this file first.
Keep it short (100 - 150 lines). Detail lives in the linked docs.

## Project Overview

**[Project name]** — [One or two sentences: what it does, who it is
for, and the problem it solves.]

Full product definition, goals and scope: [context/PROJECT.md](context/PROJECT.md)

## Tech Stack

| Layer     | Technology | Version   |
| --------- | ---------- | --------- |
| Runtime   | [Node.js]  | [22.x]    |
| Framework | [Next.js]  | [15.x]    |
| Language  | [TypeScript] | [5.x]   |
| UI        | [Tailwind + shadcn/ui] | [x.y] |
| Database  | [PostgreSQL + Prisma] | [x.y] |
| Auth      | [Clerk]    | [x.y]     |

Pin exact versions in the lockfile. Do not upgrade a dependency
unless the task says to. Roles and system boundaries:
[context/ARCHITECTURE.md](context/ARCHITECTURE.md)

## First-Run Commands

```bash
[cp .env.example .env.local]   # then fill in the values
[npm install]                  # install dependencies
[npm run db:migrate]           # create the local database schema
[npm run dev]                  # start the dev server at [http://localhost:3000]
make check                     # confirm the repo is consistent (lint, types, tests, build)
```

## Hard Constraints

Non-negotiable. If a task seems to require breaking one, stop and ask.

1. [e.g. Never commit secrets. Secrets live in `.env.local` only.]
2. [e.g. Enforce auth and ownership checks before every mutation.]
3. [e.g. Do not edit `components/ui/*` (generated). Add components via the CLI.]
4. [e.g. Do not add a dependency without approval.]
5. [e.g. Do not run destructive database commands against non-local databases.]
6. Every invariant in [context/ARCHITECTURE.md](context/ARCHITECTURE.md) holds.

## Docs Map

Read what the task needs, not everything. Order when in doubt:

| Doc | Read it for |
| --- | ----------- |
| [context/PROJECT.md](context/PROJECT.md) | Product definition, goals, scope |
| [context/ARCHITECTURE.md](context/ARCHITECTURE.md) | Stack, boundaries, storage, auth, invariants |
| [context/UI-CONTEXT.md](context/UI-CONTEXT.md) | Theme, tokens, component conventions |
| [context/CODING-STANDARDS.md](context/CODING-STANDARDS.md) | Implementation rules |
| [context/AI-WORKFLOW-RULES.md](context/AI-WORKFLOW-RULES.md) | Scoping, splitting work, verification |
| [context/PROGRESS.md](context/PROGRESS.md) | Current state, task list, next steps |
| [context/DECISIONS.md](context/DECISIONS.md) | Decisions made and why |
| [context/specs/](context/specs/) | One spec per feature unit (`00-build-plan.md` first) |

If implementation changes architecture, scope, or standards, update the
relevant doc before continuing.

## At session start (clock in)

1. Read `context/PROGRESS.md` for current state
2. Read `context/DECISIONS.md` for important decisions
3. Run `make check` to confirm the repo is in a consistent state
4. Continue from the "Next Steps" section of `PROGRESS.md`

If `make check` fails before you have changed anything, report it and
fix or log it first. Do not build on a broken baseline.

## Before session end (clock out)

1. Update `context/PROGRESS.md`: move items only when their "Done when"
   condition is verified; record blockers and session notes
2. Log any new decision in `context/DECISIONS.md`
3. Run `make check` to confirm a consistent state
4. Confirm with the user, then commit all completed work
