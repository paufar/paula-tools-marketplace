# Existing projects

Rules for [SKILL.md](SKILL.md) steps 2, 5 and 6 in Existing mode.

## Where old content goes

| Old content | Feeds |
| ----------- | ----- |
| Product description, goals, user flows, feature lists, roadmap scope | `PROJECT.md` |
| Stack, folder structure, data model, storage, auth, invariants, design docs | `ARCHITECTURE.md`, `local-docs/architecture.html` |
| Design system, colors, fonts, component notes, style guide | `UI-CONTEXT.md` |
| Lint and style rules, code conventions, contributing guidelines about code | `CODING-STANDARDS.md` |
| How to work on the repo, PR and review process, agent instructions (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`) | `AI-WORKFLOW-RULES.md`, `AGENTS.md` |
| TODO lists, roadmaps, changelogs of in-flight work, status notes | `PROGRESS.md` |
| ADRs, "why we chose X" notes | `DECISIONS.md` (keep the original date and reasoning) |
| Feature specs, PRDs, tickets written as docs | `context/specs/` |
| Install steps, env vars, deployment, troubleshooting | `local-docs/setup.md` |
| Personal notes about what the user wants to learn or get out of the project | `local-docs/goal.md` (private, never copied into committed files unless cleared) |

Sort by content, not by filename. One file often feeds several templates, and several files can feed one.

Environment files carry facts too: `package.json` (or the language's manifest) supplies versions and scripts for `AGENTS.md`, `Makefile` and `local-docs/setup.md`. Label them as a source the same way, for example *"From `package.json`"*.

## Reading sources

- Prefer the newest information. When sources disagree, show both with their file names and ask which holds.
- Mark stale material: references to files, tools or decisions that no longer exist in the repo. Check against the code before offering it.
- Content that does not fit a template's purpose (marketing copy, tutorials, API reference) is not migrated. Its file's fate is `keep`.

## Fates

- **absorb and delete**: everything useful lands in a template, and the file has no other job. Typical: old agent instruction files, scratch notes, TODO files, design notes, ADR folders once logged.
- **keep**: the file serves readers the templates do not. Default for `README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, anything under `.github/`, and API or user documentation. Still read them as sources. A README can fill `PROJECT.md` and remain.
- **ignore**: nothing relevant. Leave it untouched.

Recommend a fate per file with a one-line reason. When a file mixes both kinds of content, recommend `keep` and say what was extracted.

## Showing existing content

Every piece of prefilled content carries its source file name when shown to the user:

> From `docs/architecture.md`: "Services talk over a message queue; the API never calls workers directly."
> Use as is, edit, or replace?

Cite the source in `DECISIONS.md` entries and in the final summary. The templates themselves stay free of source annotations.

## Conflicts with template filenames

Existing `AGENTS.md`, `CLAUDE.md` and `context/*.md` are read in step 2 like any other source. Step 3 moves them to `.init-project-old/`, so the template copy never overwrites unread content. Step 6 deletes the folder once the user confirms.

## Existing progress

An existing project already has done work. Ask the user what to record:

- One `Done` baseline item describing the existing state, with a checkable "Done when" (a passing command) and real evidence from running it.
- In-flight work from old TODOs into Next Steps, one item at a time, each with a "Done when". Items without a checkable condition go to Open Questions.
- At most one item In Progress.
