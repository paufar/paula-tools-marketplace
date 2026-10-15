---
name: init-project
description: Initialize a new or existing project from the AI project foundation, migrate useful content from existing markdown files, and fill in every template with the user through discussion.
disable-model-invocation: true
argument-hint: "[resume] [target directory, defaults to the current one]"
---

# Init project

Set up a project from the AI project foundation, then fill in every template section by discussing it with the user. The user makes each decision. You draft, they steer.

Two modes, chosen in step 1:

- **New**: nothing to migrate. Skip steps 2 and 6.
- **Existing**: the project already has markdown docs. Their useful content prefills the templates, and the old files are retired once absorbed. Read [EXISTING.md](EXISTING.md) before step 2.

Template source: `${CLAUDE_PLUGIN_ROOT}/templates`. If that folder is missing or the path did not resolve, ask the user where the foundation's `templates/` folder lives.

The per-file question lists are in [SECTIONS.md](SECTIONS.md). Read the entry for a file when you reach it, not before.

## The tracker

`project-initialization.md` in the target root shows the user where the run stands. Create it right after step 1, update it at every step, and delete it as the last act of step 8.

Format:

```markdown
# Project Initialization

Target: [path] · Mode: [New | Existing] · Started: [YYYY-MM-DD HH:MM] · Updated: [YYYY-MM-DD HH:MM]

## Steps

| # | Step | Status | Notes |
| - | ---- | ------ | ----- |
| 1 | Choose the target and mode | Done | |
| 2 | Inventory existing docs | Pending | [Skipped in New mode] |
| 3 | Copy the templates | Pending | |
| 4 | Gitignore local docs | Pending | |
| 5 | Fill in the templates | Pending | see below |
| 6 | Retire old docs | Pending | [Skipped in New mode] |
| 7 | Verify | Pending | |
| 8 | Hand over | Pending | |

## Fill-in (step 5)

| File | Status | Source | Notes |
| ---- | ------ | ------ | ----- |
| local-docs/goal.md | Pending | | |

(one row per file in the step 5 list)

## Existing docs (Existing mode)

| File | Fate | Absorbed into |
| ---- | ---- | ------------- |

## Deferred

- [Section, what it blocks]
```

Status values: `Pending`, `In progress`, `Done`, `Skipped`. Fill-in rows also use `Drafting` (draft shown to the user), `Approved`, and `Deferred`. **Source** names `user` or the old file the content came from.

Update rules:

- Mark a step `In progress` when you start it and `Done` when its "Done when" holds. Put anything the user needs to know in Notes.
- In step 5, update the file's row at each change: `Drafting` when the discussion starts, `Approved` when the user approves, `Deferred` when a section is skipped.
- Refresh `Updated` on every write.
- Skipped steps get `Skipped` and a reason.
- Keep it to the format above. It is a status board, and detail lives in the templates.

Resume: a `project-initialization.md` in the target means an earlier run stopped. The tracker and the files on disk are all you have, since the earlier conversation is gone.

- `/init-project resume [directory]` resumes without asking. If there is no tracker, say so and stop.
- `/init-project` with a tracker present shows its status and asks whether to resume or start over (delete the tracker and begin at step 1).

To resume: read the tracker, re-run the `Done when` of every `Done` step before trusting it, and continue from the first step that is not `Done`. In step 5, skip `Approved` and `Deferred` rows. For a `Drafting` row, read the file as written and continue from its remaining placeholders, and for `Pending` rows start the discussion as normal. In Existing mode the old files are still in `.init-project-old/` and the sources column in the tracker says where content came from.

## 1. Choose the target and mode

Arguments are `$ARGUMENTS`. A leading `resume` word is the resume keyword (see The tracker), and the rest is the target. The target is that path, or the current directory when empty. A directory literally named `resume` is written `./resume`. Confirm the path with the user. On resume, the tracker already records the path and mode: confirm them and skip the rest of this step.

Find markdown files in the target (`*.md`, `*.mdx`), skipping `node_modules`, `.git`, `vendor`, build output, `.claude/` and `project-initialization.md`. Propose **Existing** when any turn up, otherwise **New**, and let the user choose.

Then create the tracker, following "The tracker" above, with mode and start time filled in and step 1 `Done`. Tell the user where it is.

Done when: the user confirmed the path and the mode, and `project-initialization.md` exists.

## 2. Inventory existing docs (Existing mode)

Read every markdown file found. For each, decide which template sections its content could fill, following [EXISTING.md](EXISTING.md).

Show the user a table: file, what it holds, the template sections it feeds, and a proposed fate (absorb and delete, keep, or ignore). The user adjusts the table.

Done when: the user approved the table. Every file has a fate.

## 3. Copy the templates

Copy the **contents** of the template source into the target: `AGENTS.md`, `CLAUDE.md`, `Makefile`, `context/`, `local-docs/`. The foundation's root files (`README.md`, `foundation-overview.html`, root `AGENTS.md`, `CLAUDE.md`, `.claude/`) stay behind. Create `context/specs/`.

When a template filename already exists in the target, move the existing file to `.init-project-old/` (keeping its relative path) and copy the template in. Nothing is lost, and step 2 already read it. In New mode with a conflict, ask keep, overwrite or merge per file.

Done when: `ls` of the target shows every template file and none of the foundation's root files, and every displaced file sits in `.init-project-old/`.

## 4. Gitignore local docs

Add `local-docs/` to the target's `.gitignore`. Create the file when absent. Skip when the line is already there.

Done when: `grep -x 'local-docs/' .gitignore` matches exactly once.

## 5. Fill in the templates

Work in this order, because each file builds on the ones before it:

1. `local-docs/goal.md` (private, see below)
2. `context/PROJECT.md`
3. `context/ARCHITECTURE.md`
4. `context/UI-CONTEXT.md`
5. `context/CODING-STANDARDS.md`
6. `context/AI-WORKFLOW-RULES.md`
7. `AGENTS.md`
8. `Makefile`
9. `context/PROGRESS.md`
10. `context/DECISIONS.md`
11. `context/specs/00-build-plan.md`, then the first spec
12. `local-docs/setup.md`
13. `local-docs/architecture.html`

### The private goal

`local-docs/goal.md` holds what the user wants to get out of the project for themselves, such as learning a skill or trying a tool or plugin. It is gitignored and stays private. Tell the user this before asking the first question.

It comes first because it shapes everything after it:

- **Options**: when offering options for a stack, tool or plugin choice, include the ones that match a learning target from `goal.md` and note the match to the user in the conversation.
- **Approach**: draft the "Working With the User" section of `AI-WORKFLOW-RULES.md` from "How I Want the Agent to Help" and "Boundaries".
- **Cleared for Public Files** is the only route from `goal.md` into a committed file. Propose wording for each item, aimed at directing the agent and free of personal detail (for example "Explain new concepts briefly the first time they appear", not "the user is a beginner at X"). The user approves each row. Unapproved items stay private, and their table row stays empty.
- Never quote, paraphrase or link `goal.md` in a committed file beyond the approved wording. That includes `DECISIONS.md` reasoning: give the reason the user cleared, or a neutral one.

For each file:

1. Read its entry in [SECTIONS.md](SECTIONS.md) and the template's section headings.
2. Discuss it section by section. Ask **one question at a time**. For each, offer two or three concrete options built from what the user already told you, mark your recommendation, and say why. The user can pick one, answer in their own words, skip, or defer.
3. **Existing content comes first.** When a section has content from an existing file, show it before asking anything, labelled with its source, for example: *"From `docs/architecture.md`: [the content, quoted or closely summarized]"*. Then ask whether to use it as is, edit it, or replace it. Ask new questions only for what the sources leave open or contradict.
4. Reflect earlier answers back. When a new answer contradicts an earlier one, or two sources disagree, raise it before writing.
5. Write the file. Replace every `[bracketed]` placeholder with the user's answers, and delete the example text.
6. Show the user the result and ask for changes. Apply them.

A skipped or deferred section keeps its placeholder, and you add an entry to Open Questions in `context/PROGRESS.md` naming the file, the section, and what it blocks.

Record each real choice (stack, auth, storage, anything the user weighed options for) in `context/DECISIONS.md` with the reasoning they gave. Fill `DECISIONS.md` from these as you go, and delete its example entry. Decisions found in existing docs go in with their original reasoning and source.

Done when, per file: the user approved the draft, no placeholder remains except deferred ones logged in Open Questions, and the file is 100 - 150 lines. Under 100: ask the user whether a section is missing detail, and leave the file as it is when they say no. Over 150: move detail into a linked doc.

`AGENTS.md` must not reference `local-docs/`.

## 6. Retire old docs (Existing mode)

Fate `absorb and delete` files go only after every piece of useful content from them landed in a template, or the user chose to drop it.

1. Re-read each file to delete. Confirm every useful piece appears in a template, or that the user dropped it. Fill any gap before continuing.
2. List each file to delete with the sections it fed. Include `.init-project-old/`.
3. Ask the user to confirm the deletion. Delete only on a clear yes, and only the confirmed files.
4. Content the user wants kept but that fits no template stays in place, and its file is removed from the delete list.

Done when: the user confirmed, the confirmed files and `.init-project-old/` are gone, and `git status` (when the project is a repo) shows only the deletions you listed.

## 7. Verify

1. Search the target for leftover `[` placeholders, leaving out `project-initialization.md`. Every hit is either a deferred item listed in Open Questions or a bug you fix.
2. Run `wc -l` on each markdown template and report any outside 100 - 150.
3. Check `Makefile`'s `check` target no longer exits with the stub failure, or that the user chose to defer it and it is logged.
4. Check `context/PROGRESS.md` lists Next Steps in order, each with a Done when, and has at most one item In Progress.
5. Check `git check-ignore local-docs/goal.md` prints the path, and that no committed file mentions `goal.md` or contains wording that is not in its "Cleared for Public Files" table.

Done when: the checks pass or each exception is logged in Open Questions.

## 8. Hand over

Summarize for the user: files created, what from `goal.md` went into committed files (private items stay unlisted), content migrated and from which file, files deleted, sections deferred, decisions logged, and the first task in `context/PROGRESS.md`. Point out that the next session starts by clocking in from `AGENTS.md`.

Then mark step 8 `Done` and delete `project-initialization.md`, once every row in it is `Done` or `Skipped`. When the run stops before that, leave the tracker in place so the next run can resume.

Do not commit. Ask the user before creating a commit.
