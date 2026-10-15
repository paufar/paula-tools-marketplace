---
name: close-session
description: Close off a session by writing a detailed SESSION_SUMMARY.md (what the session was about, where it got to, what happens next) into a tmp/ directory. Separate from PROGRESS.md, which tracks the project only.
disable-model-invocation: true
argument-hint: "[focus or extra notes. Optional]"
---

# Close session

Write a hand-off note for this session so the user, or a fresh agent, can pick it up cold. The session may be about the project, or about something else entirely (research, a question, another repo, planning). Summarise what actually happened, whatever the topic.

This is not `context/PROGRESS.md`. PROGRESS.md is the project's record and follows the project's clock-out rules. This skill never edits PROGRESS.md or any other project file. If the session produced project progress, mention it in the summary and say PROGRESS.md still needs its own update.

`$ARGUMENTS`, if given, is a focus or extra notes from the user. Weight the summary towards it.

## 1. Gather from the conversation

Work from this session's conversation first. Only run commands to confirm facts you will state: `git status` and `git diff --stat` for what changed, `git log` for commits made this session. Skip them if the session touched no repo.

Collect:

- the goal or question the session started with, and how it shifted
- what was done, found or decided, and the reasons
- files created, edited or deleted, with paths
- things tried that failed or were dropped, and why
- open questions, blockers, and anything waiting on the user
- open items and to-dos, including ones only mentioned in passing, half-formed ideas, "we should also...", and follow-ups that are not yet project tasks or in PROGRESS.md
- the concrete next steps

Label anything you are unsure of as **unverified**. Do not invent outcomes, reasons or test results. If something was not run, say it was not run.

## 2. Write the file

Path: `tmp/SESSION_SUMMARY.md`, a local folder under the current working directory (the project the skill is run in), not the system `/tmp`. Create `tmp/` if it does not exist.

If the file already exists, keep it and add the new section at the top, below the title. Never overwrite earlier sections.

Use this shape, with a dated heading per run (date, and a short topic):

```markdown
# Session summary

## YYYY-MM-DD: [short topic]

### Topic
One or two sentences: what this session was about, and whether it relates to the project.

### What happened
Chronological or by theme. Detailed enough to follow without the transcript: what was asked, what was found, what was decided and why.

### State right now
What is done, half done, and untouched. Files changed (path, one line each). Anything running or uncommitted.

### Decisions and findings
Each with its reason. Mark unverified items.

### Dead ends
What was tried and abandoned, so it is not repeated.

### Open questions and blockers
What is unresolved, and who or what it waits on.

### Open items and to-dos
A checklist (`- [ ]`) of everything still outstanding from the session, even if it was never defined as a project task. Include loose ideas and passing mentions, each with enough context to act on. Note which ones are not yet tracked anywhere, so they can be promoted to project tasks later.

### Next steps
Ordered, concrete, each doable without re-reading the session. Start with the very first action.

### To resume
Where to look first: files, commands, links, and one line to paste into a new session.
```

Drop a sub-heading only if it truly has nothing to say. Write "None" rather than padding.

## 3. Keep it out of git

After writing, run `git check-ignore -q tmp/SESSION_SUMMARY.md` if in a git repo. If it is not ignored, tell the user and suggest adding `tmp/` to `.gitignore`. Do not edit `.gitignore`. Never run `git add`, `git commit` or `git push` in this skill.

Do not put secrets, tokens or private content in the summary. If the session involved some, refer to them by name only.

## 4. Close

Reply with the file path and a three-line recap: topic, state, first next step. Nothing more.
