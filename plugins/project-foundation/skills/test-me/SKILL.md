---
name: test-me
description: Interview the user on the goals in their private goal.md, grill their understanding, and judge whether each goal was reached.
disable-model-invocation: true
argument-hint: "[path to goal.md or project directory, defaults to local-docs/goal.md]"
---

# Test me

Interview the user on the goals they set in `local-docs/goal.md` and judge, from what they demonstrate, whether each was reached. Be relentless and fair: the user asked to be tested, so a verdict that flatters them is a failure of this skill.

`goal.md` is private. Everything this skill produces stays in `goal.md`, never in a committed file.

## 1. Load the goals

The file is `$ARGUMENTS` (a `goal.md` path, or a project directory holding `local-docs/goal.md`), or `local-docs/goal.md` in the current directory when empty. If it is missing or still holds placeholders, tell the user and stop.

Read the whole file: Goals, Learning Targets, How I Want the Agent to Help, Boundaries, How I Will Know It Worked, Notes.

Then read what the project actually contains, so questions rest on real things: `context/PROJECT.md`, `context/ARCHITECTURE.md`, `context/DECISIONS.md`, `context/PROGRESS.md`, and the code the learning targets touch (the "Where it shows up" column).

Done when: you can list every goal and learning target, and for each the success criterion from "How I Will Know It Worked". A goal with no checkable criterion gets one drafted from its wording, and the user confirms it before you start.

## 2. Set the ground rules

Tell the user, briefly:

- Questions come one at a time, and answers come from their head, with no looking things up unless a question says to.
- You will not hint or correct mid-thread. Explanations come after each goal.
- Vague answers get pushed on.
- They can say "skip" for a goal, and it is recorded as not tested.

## 3. Grill, goal by goal

Take the goals in order. For each, build a ladder of questions from the goal, its learning targets, and the real code, then climb it until the user's **ceiling** appears, the first rung they cannot stand on:

1. **Recall**: name it. What is X, what does it do here?
2. **Explain**: why. Why was it chosen over the alternative? Why does this code work this way?
3. **Apply**: a new situation. How would they add Y, or handle Z, with it?
4. **Predict**: what happens if this input arrives, this line changes, this service is down?
5. **Diagnose**: show a realistic bug or a flaw in the design (from the real code, or a small invented case) and have them find and fix it.
6. **Defend**: challenge a sound choice they made, and see whether they hold it for the right reasons or fold.

Rules for the interview:

- One question per message. Wait for the answer.
- Ask about specifics from their project, using file names and decisions from the context docs. Generic textbook questions test memory, not the goal.
- Meet a vague answer ("it handles the auth stuff") with a narrower question ("what does it do on the second request, when the session has expired?"). Repeat until the answer is specific or plainly missing.
- Check their claims against the code. A confident answer that the code contradicts counts as a miss. Say so after the thread, with the file.
- Never supply the answer, the term, or a hint inside a thread. When they are stuck, ask an easier question one rung down to find where the floor is.
- For a target whose goal is to *do* something (build, configure, write), set one small applied task in the project and have them do it. Watch, without writing it for them, per their Boundaries. Judge the result against a checkable condition.
- Ask two or three questions on a rung before moving on, so one lucky answer does not pass it.
- Rungs are for finding the ceiling, not for completing the list. Stop a thread when the ceiling is clear.

After each goal, explain the answers they missed: what was right, what was missing, and where to look. Then continue.

Done when, per goal: you found the ceiling or the user cleared every rung, and you have their answers, or a note of what they did in an applied task, as evidence.

## 4. Judge

Grade each goal against its success criterion, using what they demonstrated. Confidence and self-assessment are not evidence.

| Verdict | Means |
| ------- | ----- |
| **Reached** | Cleared the rungs the criterion needs, including apply or predict for a doing goal, with no significant misses |
| **Partly** | Solid on recall and explain, but the ceiling sits below what the criterion needs |
| **Not yet** | Cannot explain or apply what the criterion requires |
| **Not tested** | Skipped or out of time |

For each Learning Target, also state the level shown, against "Where I am now" and "Where I want to be".

Give each verdict its evidence: the questions that decided it and the answers, quoted or closely summarized. Name the ceiling. List the specific gaps and one concrete next step for each (something to practise or read, or a small task to attempt).

Be direct about the misses. Praise what was demonstrated, and no more.

Done when: every goal has a verdict, its evidence, and, unless Reached, its gaps and next steps.

## 5. Report and record

Show the user the report: a table of goals with verdicts and target levels, then the evidence and next steps per goal.

Ask before writing. On a yes, append a dated entry to the Notes section of `goal.md` with the verdicts, gaps and next steps, and offer to update "Where I am now" in the Learning Targets table to the levels shown. Change nothing else in the file.

Write only to `goal.md`. Do not touch committed files, and do not commit.

## 6. Close

Say which goals are Reached, and what to work on for the rest. Offer to run `/test-me` again once they have worked on the gaps, and to test only the goals that were not Reached.
