# Progress

> Keep this file to 100 - 150 lines. Trim finished items and old session notes as it grows.

Single source of truth for project state. The agent reads this at
session start and updates it at session end (see `AGENTS.md`).

## Current Phase

- [e.g. Not started / Phase 1: Foundation / Complete]

## Current Goal

- [What you are building right now]

## Rules for This File

1. Every item has an ID and a **Done when** condition: a specific,
   checkable statement (a command that passes, a behavior you can
   observe). "Looks good" and "works" are not conditions.
2. An item moves to Done only after its condition has been checked.
   Record how in **Evidence** (command output, test name, screen).
3. An item that cannot proceed goes to Blocked with **Blocked by**
   naming the exact thing it is waiting on.
4. Do not add an item without a Done when. If you cannot write one,
   the item is not understood yet: add it to Open Questions instead.
5. Link the spec in `context/specs/` when the item has one.
6. The WIP limit is 1: at most one item in In Progress. Finish it
   or move it to Blocked before starting the next.

Item format:

```markdown
- **[ID] [Task name]** ([spec link, if any])
  - Done when: [checkable condition]
  - Evidence: [filled in when moved to Done]
  - Blocked by: [only in Blocked]
```

## Done

- **[T-00] [Example: Repo scaffolded]**
  - Done when: `npm run dev` serves the default page and `make check` passes
  - Evidence: [2026-01-01, `make check` green, dev server on :3000]

## In Progress

WIP limit: 1.

- None yet.

## Blocked

- None yet.

## Next Steps

Ordered. The agent starts at the top after clock in.

1. **[T-01] [First unit to build]** ([context/specs/01-name.md])
   - Done when: [checkable condition]
2. **[T-02] [Second unit]**
   - Done when: [checkable condition]

## Open Questions

- [Unresolved product or technical decision. Note what it blocks.]

## Session Notes

Newest first. Only what the next session needs to resume.

- [YYYY-MM-DD] [Where things were left, gotchas, half-finished work]

Decisions and their reasoning live in [DECISIONS.md](DECISIONS.md), not here.
