---
name: interview-prep
description: Refresh the user on a repo's architecture decisions and tooling, then mock-interview them on it, shaped around a job vacancy if one is given.
disable-model-invocation: true
argument-hint: "[vacancy: URL, file path, or pasted text. Optional]"
---

# Interview prep

Get the user ready to talk about this project in an interview: a short refresher first, then a mock interview. It works on any repo, with or without the AI context template. The aim is that they can explain the project's decisions in their own words, so never put words in their mouth.

## 1. Take in the vacancy

The vacancy is `$ARGUMENTS`: a URL (fetch it), a file path (read it), or pasted text. If empty, ask once for the vacancy and say "none" is fine. With none, prep for a general technical interview on the project.

From the vacancy, note: role and seniority, must-have and nice-to-have skills, domain, and any hint of interview format. Keep this list short. It decides what to emphasise in every later step.

Done when: you can state the role in one line and list the 3-6 things the vacancy cares about most (or you have recorded that there is no vacancy).

## 2. Learn the project from evidence

Read only what exists, in this order of trust:

1. Decision records: `context/DECISIONS.md`, `context/ARCHITECTURE.md`, `context/PROJECT.md`, `context/PROGRESS.md`, any `docs/`, ADRs, `README.md`.
2. Dependencies and tooling: manifests and lockfiles (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, `Gemfile`, ...), build and CI config, Docker, linters, test setup.
3. The code: directory layout, entry points, the modules that carry the main logic.
4. History: `git log` for the shape of the work, large or reworked areas, and reversals.

Also read `local-docs/goal.md` if it exists. It is private, but it tells you where the user is shaky before the interview starts: the Learning Targets ("Where I am now" vs "Where I want to be"), and any past `/test-me` verdicts and gaps in Notes. Treat targets that are still below their goal, and any "Partly" or "Not yet" verdict, as known weak spots. Never quote `goal.md` in anything outside `local-docs/`.

Label every claim as **documented** (a file says so), **visible** (the code shows it) or **inferred** (you are guessing the reason). A reason you cannot find is "not recorded". Never invent a rationale. Unrecorded reasons become questions for the user in step 4.

Done when: you can list the main architecture decisions and every significant tool or package, each with its evidence label.

## 3. Brief the user

Give a refresher they can read in a few minutes. Plain, scannable, no padding:

1. **The 30-second pitch**: what the project is, who it is for, the one thing that makes it interesting.
2. **Architecture decisions**: for each major one, a row of *Decision / Why / Alternative not taken / Trade-off accepted / Evidence label*. Cover the 5-8 that an interviewer would most plausibly probe.
3. **Tools and packages**: a table of *Tool / What it does here / Why it was chosen / Alternative*. Group by purpose. Skip trivial transitive dependencies.
4. **Hard parts and honest weak spots**: bugs, rework, shortcuts, things you would do differently, taken from history and the code. Interviewers ask "what would you change?", so the user needs an answer. Add a **known shaky areas** list from `goal.md`, if there was one, so they see what you will press on.
5. **Vacancy map** (only with a vacancy): each thing the vacancy cares about, matched to where the project shows it, with a suggested lead story. Then **gaps**: requirements the project does not show, with an honest way to talk about them (adjacent experience, what they would learn first). Do not stretch the project to cover a gap.

Mark every "not recorded" reason with a question mark, and tell the user these are the things to settle in their own head before the interview.

Done when: the briefing is shown. Ask whether anything is wrong or missing, and correct it. The user knows the real history better than the files do.

## 4. Mock interview

Ask how long they want (default about 10 questions) and whether they want **coach** mode (brief feedback after each answer, the default) or **cold** mode (no feedback until the end).

Rules:

- One question per message. Wait for the answer.
- Ask about this project's real specifics: name files, decisions, packages. Generic questions are a last resort.
- Tilt the mix toward the vacancy: its must-haves get the most questions. Without a vacancy, spread evenly. Where a vacancy must-have overlaps a known shaky area from `goal.md`, ask there first and more than once.
- Push on vague answers with a narrower follow-up. Stop a thread when the answer is clear or plainly missing.
- When the user answers "I don't know why", ask what they would reason it was, and note it as a gap to settle.
- Check their claims against the code. If the code contradicts a confident answer, say so after the answer, with the file.
- In coach mode, after each answer give two or three lines: what landed, what was missing, a sharper phrasing. Do not rewrite their whole answer. Do not supply the answer before they have tried.
- Keep to a realistic tone: an interviewer, not a quiz master.

Cover a spread of these, picking what fits the project and vacancy:

| Type | Example shape |
| ---- | ------------- |
| Pitch | "Walk me through this project." |
| Decision | "Why X over Y here?" |
| Tool | "What does Z give you that the standard library does not?" |
| Trade-off | "What did that choice cost you?" |
| Change | "A new requirement lands: how does your design cope?" |
| Failure | "What happens when this service is down, or this input is bad?" |
| Hindsight | "What would you do differently?" |
| Behavioural | A story from the project's history: conflict, mistake, scope call, a bug that taught something |
| Vacancy | A question the job description makes likely, tied to the project |
| Gap | A requirement the project does not show, asked as an interviewer would |
| Curveball | One unexpected question, to practise staying calm and structured |

Done when: the agreed number of questions is done, or the user says stop.

## 5. Debrief

Give a short report:

- **Strong**: answers that were specific and well reasoned.
- **Shaky**: questions where the answer was vague, wrong against the code, or missing, each with the file or doc to re-read.
- **Sharper answers**: for the two or three weakest, a tighter version built only from facts the user stated or the project shows.
- **Stories to have ready**: 2-3 project stories that fit the vacancy, each with one line on the point it proves.
- **Before the interview**: a short checklist of what to re-read or settle.

Ask before saving. If they say yes, write the briefing and debrief to `local-docs/interview-notes.md`, adding a dated section per run (role or "general" in the heading) rather than overwriting earlier ones. Before writing, run `git check-ignore -q local-docs/interview-notes.md` and `git ls-files --error-unmatch local-docs/interview-notes.md`. Write only if the first succeeds (ignored) and the second fails (not tracked). If the path is not ignored, is already tracked, or the repo has no `local-docs/`, do not write there: say why and offer `~/interview-prep/<repo-name>-<date>.md` instead (outside any repo). If the repo is not a git repository, use that fallback too.

These notes must never be committed. Never run `git add`, `git commit` or `git push` in this skill, never use `git add -f`, and never edit `.gitignore` to make the path ignored. If the user asks you to commit them, decline and tell them why. Write nowhere else, and change nothing in `goal.md`.

## 6. Close

Offer a second round: only the shaky areas, or a different vacancy.
