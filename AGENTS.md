# AGENTS.md

Instructions for working on this repo, the AI project foundation. This file
is not part of the templates and is never copied into a project.

## Layout

This repo is a Claude Code plugin marketplace named `paula-tools`
(`.claude-plugin/marketplace.json`). It holds two plugins. This repo is the
source of truth for every skill and template: nothing is kept in
`~/.claude/skills/`, so edit the files here only.

| Path | What it is | Copied into projects |
| ---- | ---------- | -------------------- |
| `AGENTS.md` (this file, repo root) | Agents maintaining this repo | No |
| `CLAUDE.md` (repo root) | Pointer to this file | No |
| `.claude-plugin/marketplace.json` | The marketplace catalogue: lists both plugins. Add every new plugin here | No |
| `plugins/project-foundation/` | Plugin with `/init-project`, `/test-me` and the templates | No |
| `plugins/project-foundation/skills/init-project/` | The `/init-project` skill that copies and fills in the templates. Reads them from `${CLAUDE_PLUGIN_ROOT}/templates` | No |
| `plugins/project-foundation/skills/test-me/` | The `/test-me` skill that tests the user against `goal.md` | No |
| `plugins/project-foundation/templates/` | The templates. Only their contents are copied into a project | Yes |
| `plugins/project-foundation/templates/AGENTS.md` | Agents working in a project built from the template | Yes |
| `plugins/project-foundation/templates/CLAUDE.md` | Pointer to the project's `AGENTS.md` | Yes |
| `plugins/learning-tools/` | Plugin with `/interview-prep` and `/close-session` | No |
| `plugins/learning-tools/skills/interview-prep/` | Refreshes the user on any repo and mock-interviews them. Reads `local-docs/goal.md` (Learning Targets, Notes) for known weak spots and saves to `local-docs/interview-notes.md` | No |
| `plugins/learning-tools/skills/close-session/` | Writes a hand-off `tmp/SESSION_SUMMARY.md` for any session, separate from `PROGRESS.md` | No |

In the rest of this file, `templates/` means
`plugins/project-foundation/templates/`.

Only the contents of `templates/` are copied into a new project. Never copy
the root files, and never put repo-maintenance rules (like the sync rule
below) into `templates/`, or they will leak into every future project.

Skills are invoked with the plugin name as a prefix, for example
`/project-foundation:init-project`. Bump `version` in the plugin's
`.claude-plugin/plugin.json` when its skills or templates change, or installed
copies will not update.

## Sync rule

Any time a template changes, update the foundation overview and every other
file affected by the change, in the same change. Do not leave them for later.

A template change is anything under `templates/`: adding, removing, renaming
or moving a file, or changing what a file holds, its sections, or its rules.

Check each of these and update the ones that are affected:

| File | Update when |
| ---- | ----------- |
| [foundation-overview.html](foundation-overview.html) | Any template change: file layout, the card for that file, the rules table, the initialization steps |
| [README.md](README.md) | File tree, the "What is in templates" table, the rules list, the usage steps |
| `templates/AGENTS.md` | Docs Map rows, first-run commands, clock in / clock out steps |
| `templates/CLAUDE.md` | The entry point or the list of docs it summarizes changes |
| `templates/context/AI-WORKFLOW-RULES.md` | Keeping Docs in Sync list, Protected Files, checklist |
| `templates/local-docs/architecture.html` | Anything that changes `context/ARCHITECTURE.md` sections |
| `templates/local-docs/setup.md` | Project layout section, commands, prerequisites |
| `plugins/project-foundation/skills/init-project/` | A template file is added, removed or renamed, or a section changes: update the copy, fill-in order and verify steps in `SKILL.md`, the questions in `SECTIONS.md`, and the mapping and delete rules in `EXISTING.md` |
| `plugins/project-foundation/skills/test-me/SKILL.md` | The section names in `templates/local-docs/goal.md` change: the skill reads Goals, Learning Targets, How I Will Know It Worked, Boundaries and Notes |
| `plugins/learning-tools/skills/interview-prep/SKILL.md` | The Learning Targets or Notes sections of `goal.md` change, or `local-docs/` is renamed or dropped from the gitignore |
| `.claude-plugin/marketplace.json` and the plugins' `plugin.json` | A plugin or skill is added, removed or renamed, or its description changes |
| Cross-references between templates | A file is renamed or moved: search for the old name in every file |

Before finishing:

1. Search the repo for the old name of anything renamed or removed.
2. Confirm every file under `templates/` appears in the README tree and in
   the overview's file layout and has its own card in the overview.
3. Confirm the two HTML files still parse and the README tree matches disk.
4. Say which files you updated, and which you checked and left alone.

## Template rules

- Each markdown template stays between 100 and 150 lines once filled in.
- `local-docs/` is gitignored in projects, so `templates/AGENTS.md` must not
  reference it.
- `local-docs/goal.md` is private: never quote or link it from a committed
  file. Only the wording in its "Cleared for Public Files" table may reach one.
- Templates use `[bracketed]` placeholders. Do not put real project content in them.
