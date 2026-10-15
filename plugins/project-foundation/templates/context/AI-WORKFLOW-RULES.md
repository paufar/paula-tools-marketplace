# AI Workflow Rules

> Keep this file to 100 - 150 lines once filled in. Move detail into a linked doc rather than growing it.

## Approach

[Describe the overall development approach — e.g. Build
this project incrementally using a spec-driven workflow.
Context files define what to build, how to build it, and
the current state of progress. Always implement against
these specs — do not infer or invent behavior from scratch.]

## Scoping Rules

- Work on one feature unit at a time
- Prefer small, verifiable increments over large
  speculative changes
- Do not combine unrelated system boundaries in a
  single implementation step

## Work in Progress Limit

The WIP limit is 1. `PROGRESS.md` holds at most one item under
In Progress.

- Finish the item (moved to Done with evidence) or move it to
  Blocked before starting another
- A new idea that appears mid-task goes to Next Steps or Open
  Questions, not In Progress
- A half-finished item is never left behind to start a new one

## When to Split Work

Split an implementation step if it combines:

- [Concern one — e.g. UI changes and background task changes]
- [Concern two — e.g. Multiple unrelated API routes]
- [Concern three — e.g. Behavior not clearly defined in
  the context files]

If a change cannot be verified end to end quickly,
the scope is too broad — split it.

## Handling Missing Requirements

- Do not invent product behavior not defined in the
  context files
- If a requirement is ambiguous, resolve it in the
  relevant context file before implementing
- If a requirement is missing, add it as an open question
  in `PROGRESS.md` before continuing

## Working With the User

How the agent collaborates in this project:

- [Explanation style — e.g. Explain new concepts briefly the
  first time they appear]
- [Tools, plugins or techniques to prefer — e.g. Use [tool]
  for [task] where it fits]
- [Where the user wants to drive — e.g. Show the approach, then
  let the user write the next one]

## Protected Files

Do not modify the following unless explicitly instructed:

- [e.g. components/ui/* — generated UI library components]
- [e.g. Any third-party library internals]

## Keeping Docs in Sync

Update the relevant context file whenever implementation
changes:

- System architecture or boundaries
- Storage model decisions
- Code conventions or standards
- Feature scope
- Local docs setup and architecture

## Before Moving to the Next Unit

1. The current unit works end to end within its defined scope
2. No invariant defined in `architecture.md` was violated
3. `PROGRESS.md` reflects the completed work, and each item moved
   to Done has its "Done when" condition verified with evidence
4. Any new decision is logged in `DECISIONS.md`
5. `make check` passes
