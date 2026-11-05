---
name: no-loose-ends
description: Write tickets, Linear issues, user stories, specs, implementation plans, PRDs, runbooks, articles, announcements, READMEs, and emails that leave the reader nothing to guess, applying the writing rules learned from past Nitpicker reviews. Use this whenever the user asks to write, draft, create, rewrite, or clean up any ticket, issue, story, spec, plan, brief, article, post, doc, or message that someone else will act on, even if they don't mention rules or Nitpicker. It writes; its partner skill `nitpicker` reviews.
---

# No Loose Ends

Write the text so a capable newcomer could act on it without asking a single question. The `nitpicker` skill finds gaps after the fact, and every gap it finds becomes a rule here. This skill applies those rules while writing, so the same gap doesn't come back.

## 1. Load the rules

Read both rule files before drafting:
- **Team rules:** `references/rules.md` in this skill's folder. These are shared and changed by PR.
- **Personal rules:** `~/.claude/no-loose-ends/rules.md`, if it exists. These are learned on this machine from Nitpicker runs. If a personal rule conflicts with a team rule, the personal rule wins.

Each rule is about a **kind of sentence**, not a subject: "When you write <kind of sentence>, always include <element>." Use the rules whose **Applies to** line matches what you're writing. While drafting and again when checking, look at each sentence and ask whether it's one of the kinds a rule names. If it is, make sure it has what the rule says to include. The example in a rule only illustrates it. Apply the rule to any sentence of that kind, whatever the topic.

## 2. Gather before you write

- Collect what the user gave you: notes, a PRD, a Slack thread, an old ticket, a repo.
- **Look up every named thing before writing it down**: repos, files, functions, permission names, config keys, routes, people, teams. Copy the exact name from the source, with a locator. If it doesn't exist yet, write `new: <name>` and where it will be defined.
- **For a ticket**, use the team's shape. If the ticket goes into Linear, fetch one or two recent tickets from the same team or project and mirror their sections. If there's nothing to mirror, use the default shapes below.

## 3. Draft with these built-in habits

These are the reverse of what Nitpicker flags:
- **No vague words.** Replace "should", "just", "as needed", and "appropriately" with the rule that decides. If either option is fine, say "either X or Y is accepted".
- **Point, don't gesture.** "Follow the existing pattern" becomes the file and function to copy.
- **Edges are part of the spec.** Say what happens with empty, missing, duplicated, or malformed input, and on failure, timeout, concurrent use, or a second run, wherever these apply.
- **Tests have a command and an expected result.** Name which tests, run by which command, showing what.
- **Count the "all".** If you write "all routes" or "every pair", say how many and where you counted them.
- **Done is something you can see.** Acceptance criteria describe an observable result, not "works" or "looks right".
- **For prose:** name the audience, define terms at first use, give dates with year and timezone, use named owners, and put steps in the order they happen.

## 4. Never invent decisions

When you don't know something, don't hide the gap with a vague word or a plausible guess. Put it in an **Open questions** section with a `[placeholder]` in the text, and name who decides when you know. A ticket with three honest open questions is better than one that looks complete and isn't.

## 5. Check before handing over

Go through the draft against each loaded rule and the habits in step 3, and fix what fails. Then tell the user, in your reply and not in the document: "Checked against N rules. M open questions left for you." List the open questions.

Suggest `/nitpicker` as a last pass for anything high-stakes. Its findings feed new rules back here.

Write the draft in the chat, or to a file if the user names one. Only create or update a Linear ticket if the user asks, because that's visible to the whole team.

## Default shapes

Use these only when there's no team template to mirror.

**Ticket**: Title (the outcome, in plain words) · Why · Scope (repo, files or `[to confirm by <who> before <when>]`, do not touch) · Acceptance criteria (observable) · Proof (environment, data, command, expected result) · Edge cases · Decisions (date and who) · Open questions · Out of scope.

**Plan or spec**: Goal · Current state (with locators) · Steps (each with files touched and how to check it's done) · Failure and rollback · Test commands · Open questions.

**Article or prose**: one line on the audience and the job of the piece (not published) · key facts with dates and owners · steps in order · terms defined at first use · links.

## Rule format

Both rule files use this format, which Nitpicker writes too:

```markdown
### <The kind of sentence, e.g. "Announcing a change">
**When you write:** <a kind of sentence or statement, described without any subject or domain>
**Always include:** <the element(s) that kind of sentence needs>
**Why:** <what the reader gets wrong without it>
**Before → after:** "<weak line>" → "<strong line>"
**Applies to:** tickets | specs | plans | articles | all
**Seen:** <count> (<ticket or doc id>, <YYYY-MM-DD>; …)
```
