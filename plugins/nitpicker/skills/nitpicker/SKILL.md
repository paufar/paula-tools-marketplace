---
name: nitpicker
description: Nitpick a ticket, plan, spec, PRD, article, or any piece of instructional text until it leaves no decision to the reader, reading it as a capable newcomer with zero tribal knowledge would and surfacing every hidden decision as a ranked question with evidence. Three output modes: `ticket` (a list of questions for the author, plus recommendations), `text` (an interactive HTML page of snippet → suggested change with accept checkboxes), and `report` (a full ranked review with evidence). Every run ends with general "rules for next time" that the partner writer skill `no-loose-ends` can apply. Use this whenever the user wants a ticket, Linear issue, plan, spec, RFC, brief, article, or doc checked for ambiguity, gaps, or clarity before handing it to developers, agents, readers, or another team, including phrasings like "is this ticket ready", "poke holes in this", "what's unclear here", "would a dev have questions", "review my spec", "tighten this article", "is this clear enough", "nitpick this", or "nitpicker this".
---

# Nitpicker

Read the text the way a capable but brand-new engineer would: they are smart, they will do exactly what the text says, and they have nothing but this text and the sources around it (the repo, linked docs, the ticket's comments). Every place where they would have to *decide something alone* is a gap. Your job is to find those gaps and make them visible to the author.

The point is not pedantry for its own sake. Each unresolved decision becomes a silent guess by the reader, and wrong guesses are expensive: rework, the wrong files touched, a "done" that isn't. A question asked now costs the author a sentence.

## Parameters

Invocation: `/nitpicker:nitpicker [mode] [--blocking-only] <input>` when installed as a plugin, or `/nitpicker …` as a standalone skill. The examples below use the short form.

| Param | Values | Effect |
|---|---|---|
| `mode` | `ticket`, `text`, `report`, or omitted | Picks the output (see **Output modes**). |
| `--blocking-only` | flag | Leave out non-blocking items. Useful for a quick "can this start?" check. |
| `<input>` | pasted text, a file path, a Linear ID like `LIN-123`, or a URL | The thing to review. |

If the first argument is `rules`, don't review anything. Manage the saved writing rules instead (see **The rules command** below).

The parameters can also be given in plain language ("just the questions", "give me the accept/reject page", "only the blockers"). Map those to the modes above.

**If mode is omitted, pick one from the input** and say which you picked in one line:
- A Linear/Jira ID, or text shaped like a work item (acceptance criteria, "as a user…", tasks for someone to build) → `ticket`
- Prose meant to be read as is: an article, blog post, doc page, announcement, README section, email → `text`
- An implementation plan or spec against a repo, where evidence and locators matter most → `report`

If it's genuinely unclear, use `ticket`. It's the cheapest output and the easiest to switch from.

## Inputs and sources

- **Linear tickets**: fetch with `get_issue` (description) and `list_comments` (discussion). Comments often hold decisions that never reached the description, so read them before flagging something as missing.
- **Files / URLs**: read the whole thing. For web pages, prefer the defuddle skill if available.
- **Sources for evidence**: the repository in the working directory or one the user names, any docs the text links, and anything else the user provides. If there are no sources beyond the text, say "text only". That's fine for articles.
- **Revision**: if the text names a branch, tag, or commit, check references at that revision (`git show <rev>:<path>`, `git ls-tree <rev>`), not just the working tree.

## Method (same for every mode)

1. **Read the whole text once, end to end**, before flagging anything. Many apparent gaps are answered three paragraphs later.
2. **Read it again, sentence by sentence.** For each one, ask: *what would someone who has read only this text and the sources have to decide on their own?*
3. **Flag these on sight**, because each one hides a decision:
   - **Weasel words**: "should", "just", "simply", "as needed", "appropriately", "where relevant", "etc." Who decides, and by what rule?
   - **Pattern references**: "follow the existing pattern", "like we do elsewhere", "the usual way". Which file, which function? Search with Grep/Glob. Several candidates or none means it's a question. Exactly one means cite it, and still confirm it.
   - **Named things**: files, modules, symbols, commands, config keys, env vars, endpoints, people, teams, dashboards, products. Check that each one exists (at the given revision, if there is one). If a reference points to something that isn't there, that's a **blocking** question.
   - **Collections and inputs**: any list, lookup, payload, or user input. What happens when it's empty, missing, duplicated, or malformed?
   - **Boundaries**: anything that calls out, persists, or runs on a schedule. What happens on failure, timeout, concurrent use, partial completion, or a second run?
   - **Testing language**: "update the tests", "add tests", "make sure it works". Which tests, run by which command, expecting what output?
   - **Scope words**: "all", "every", "the relevant", "any". List what they actually cover (e.g. grep every call site). If the count would surprise the author, ask.
   - **Unobservable done-ness**: "works", "looks right", "is clean", "is fast", "is better". These can't be observed. Ask what would be observed: a number, an output, a passing check.
   - **For prose and articles**, the same idea applies to the reader: undefined terms and acronyms, an unstated audience, claims with no source, dates with no year or timezone, owners with no name, instructions whose order or trigger is only implied, and pronouns whose referent is unclear.
4. **Look for the answer in the sources first.** Attach what you find as evidence with locators (`path/to/file.ts:42`, a doc URL, or a comment's author and date). **Don't treat what you found as the answer.** The code shows what exists, and only the author can say whether that's what they intend. Keep the question open and attach the evidence: "The repo does X at `foo.py:10`. Is that the intent here?"
5. **Merge and dedupe.** Don't ask the same thing twice in different words. If one decision would settle several gaps, combine them into one item and note what it settles.

## Ranking

An item is **blocking** when a wrong guess would change the shape of the work or the meaning of the text:
- a different set of files or systems touched
- a different interface, contract, or data shape
- a different definition of done
- something hard to undo (migrations, deletions, external sends, published content)
- something that runs unattended on the guess (cron jobs, automations, agents)
- for prose: a reader would come away believing or doing something the author didn't intend

Rank blocking items by the cost of a wrong guess, highest first. Everything else is **non-blocking**: a wrong guess would be cheap to fix in review.

With `--blocking-only`, leave out non-blocking items and say how many you left out.

## Output modes

### `ticket`: questions for the author, plus recommendations

Short and easy to paste. The author should be able to answer it in one sitting. Print it in the terminal:

```markdown
# Questions before this is ready: <ticket id / title>
**Verdict:** <Ready | Ready after N quick answers | Not ready: N blocking questions>

## Must answer before work starts
1. <Question the author can answer in one sentence>
   _Why:_ <what a wrong guess would change> · _Found:_ <evidence + locator, or "nothing in repo">
2. …

## Worth answering
- <non-blocking question> (_Found:_ <locator>, if any)

## Recommendations
- <Concrete additions to the ticket that would prevent the questions recurring, e.g. "Add acceptance criterion: `npm test -- billing` passes and the invoice total matches the fixture in `tests/fixtures/inv.json`">
- <Missing sections: out of scope, rollout/rollback, owner, test command>
```

Recommendations say *what to add*, and use the author's own terms. Where the content depends on an answer, use a `[placeholder]` instead of guessing.

Don't post to Linear or edit the ticket. Afterwards, offer once: "Want me to post these as a comment on <ticket>?" Only do it if the user says yes.

### `text`: interactive accept/reject page

For prose. This mode produces an HTML page where each item shows the original snippet, what's wrong, and a suggested replacement, with a checkbox to accept it. The page includes a live preview of the revised text, "Copy revised text", "Download .md", and "Copy decisions for Claude" (a summary the user pastes back to you).

1. Do the review per **Method**. For each item, write:
   - `snippet`: an **exact, verbatim substring** of the original, long enough to occur only once. The page applies changes by find-and-replace, so a paraphrased snippet silently fails to apply.
   - `issue`: the question or gap, in one or two sentences.
   - `suggestion`: the full replacement for the snippet, not a description of it.
   - `kind`: `rewrite` when you can fix it from the text and sources alone, `question` when the fix needs the author's decision. For `question`, still write the replacement, with `[bracketed placeholders]` where the decision goes (e.g. "Deploys run at [time + timezone]"). The author fills the brackets in the textarea. Never fill a decision with your own guess.
   - `severity`, `evidence` (optional), and a sequential `id`.
2. Write the JSON to the scratchpad (schema at the top of `scripts/build_review.py`), with `original` set to the full verbatim text.
3. Build the page:
   ```bash
   python3 <skill-dir>/scripts/build_review.py <scratchpad>/review.json <scratchpad>/clarity-review.html
   ```
   If it prints a WARNING (a snippet isn't found or isn't unique), fix the JSON and rebuild. Don't publish with warnings.
4. Publish `clarity-review.html` with the Artifact tool (icon: `checklist`, description: one line naming the document). The template already meets the page contract (title, light/dark tokens, mobile layout), so don't restyle it.
5. Tell the user the link, the verdict, and the counts. Say that when they're done, they can click **Copy decisions for Claude** and paste the result here. When they paste decisions back, apply exactly the accepted changes, with their edits, to the source file if there is one, and touch nothing else.

### `report`: full ranked review

For implementation plans and specs where the evidence matters. Print it in the terminal:

```markdown
# Nitpicker review: <title>

**Sources checked:** <repo + revision / ticket + comments / docs, or "text only">
**Verdict:** <Ready | Ready after N non-blocking answers | Not ready: N blocking questions>

## Blocking questions (highest cost of a wrong guess first)
### 1. <Question>
- **Where:** "<short quote>" (section/line)
- **Why it blocks:** <what changes if the implementer guesses wrong>
- **Evidence:** <what the sources show, with locators, or "nothing found">
- **Settles:** <other gaps this answer resolves, if merged>

## Non-blocking questions
### <Section of the text>
- <question>, where "<quote>". Evidence: <locator or none>

## Verified references
<Named files, symbols, commands, and links that were checked and exist, one line each>
```

## Rules for next time (end of every mode)

A review fixes one text. A rule stops the same gap in the next text. After the output, turn the findings into writing rules for the partner skill `no-loose-ends`, which writes tickets, plans, and articles.

1. **Turn each finding into a rule about writing, not about the subject.** Take each blocking item, plus any non-blocking pattern that came up twice or more, and work through three steps:
   - **What kind of sentence was it?** Describe it without its topic: an announcement of a change, a permission ("can", "is allowed"), a reference to something the reader must find, a claim that something happens, a description of how something is checked, a soft verb, a placeholder, an instruction with steps, a comparison ("faster", "better").
   - **What was missing that the reader needed?** Name it as a general element: a date, an audience, an owner, a condition, a location, a pass mark, an order, a number.
   - **Write the rule:** "When you write <kind of sentence>, always include <element>."

   For example, the finding "The new dashboard rolls out next week" is an announcement of a change, missing the date and who it affects. So the rule is "When you announce a change, always include the exact date and who it affects."

   Test each rule: it must still make sense for a recipe, a holiday email, or a ticket on another system. If it mentions a domain (databases, permissions, dashboards, APIs), go up a level. "Check the schema allows duplicates" is about the subject. "When you write that something is allowed, include what makes it possible" is about writing.
   - Keep names, IDs, file paths, and numbers out of the When and Always include lines. They go only in the Seen line and the Before → after example.
   - Several findings often come from one kind of sentence. Write one rule for all of them.
2. **Check what already exists.** Read the team rules at `../no-loose-ends/references/rules.md`, relative to this skill's folder (both skills ship in the same plugin), and `~/.claude/no-loose-ends/rules.md` (personal rules, if any). If a rule already covers a finding, don't add a new one: increase its Seen count instead. If a finding shows that an existing rule is unclear, propose a new wording.
3. **Show at most 5**, new and updated together, under a final heading **`## Rules for next time`**. Use the rule format from `no-loose-ends` (title, When you write, Always include, Why, Before → after, Applies to, Seen). In `text` mode, put them in the terminal message after the link.
4. **Ask once:** "Save these to your no-loose-ends rules?" Only on a yes, append them to `~/.claude/no-loose-ends/rules.md`, creating the file if needed with a one-line header. Never edit the team rules file. If a rule has been seen 3+ times, suggest promoting it to the team file by PR.
5. End with one line: "Next time, ask `no-loose-ends` to write the ticket and these rules are applied while it drafts."

Skip this section when there were no findings, or when every finding is already covered by an existing rule. In that case, just bump the Seen counts after asking.

## The rules command

`/nitpicker rules [list | show <title> | promote [<title> | --ready] | remove <title>]`

This manages the writing rules that `no-loose-ends` applies. Plain-language versions work too: "show my rules", "which rules are ready for the team?", "promote the announcing-a-change rule".

The two rule files:
- **Personal:** `~/.claude/no-loose-ends/rules.md`. It may not exist yet. If it doesn't, say so, and say that rules get saved there after a review.
- **Team:** `../no-loose-ends/references/rules.md`, relative to this skill's folder. Read it from there, but never edit that copy: if installed as a plugin, it's replaced on every update. Team changes go through the source repo, as described under `promote`.

### `list` (the default)
Read both files and print a table:

```markdown
| Rule | When you write → always include | Where | Seen | Last seen |
|---|---|---|---|---|
| Announcing a change | an announcement → date + who it affects | team | 1 | 2026-11-04 |
```

Sort personal rules first, highest Seen first. After the table, add these notes, leaving out any that don't apply:
- **Ready for the team:** personal rules with Seen 3 or more.
- **Possible duplicates:** a personal rule that covers the same kind of sentence as a team rule. Suggest merging the two by raising the team rule's Seen count.
- **Stale:** rules not seen in the last 90 days. They may be noise. Suggest reviewing them, but don't remove them.

### `show <title>`
Print the full rule. Match the title loosely, and ask if more than one rule matches.

### `promote [<title> | --ready]`
Move personal rules into the team file through a PR. `--ready` means every personal rule with Seen 3 or more.

1. **Find the team repo**: the git checkout of the plugin's source, where `no-loose-ends/references/rules.md` is committed. Check `~/.claude/no-loose-ends/team-repo.txt` for a saved path. If there isn't one, ask the user for the path, confirm the rules file exists there, and save the path to that file.
2. In that repo, create a branch `rules/promote-<short-slug>` from the up-to-date default branch. Append each rule to `rules.md`. If a team rule already covers the same kind of sentence, merge into it instead: add the Seen counts and combine the sources.
3. Commit with a message listing the promoted rules, and show the diff.
4. **Ask before pushing or opening the PR**, because both are visible to the team. On a yes, push the branch and open the PR with `gh pr create`, using a body that lists each rule with its Seen count and sources.
5. After the PR is opened, ask whether to remove those rules from the personal file. Default to keeping them until the PR is merged.

If no repo is available, print the rule blocks ready to paste, and the path of the file they go into.

### `remove <title>`
- **Personal rule:** show it, confirm, then delete it from the personal file.
- **Team rule:** don't delete it locally. Offer to open a removal PR the same way as `promote`, including the reason the user gives.

## In every mode

- If the text really is clear, say so and keep the output short. Don't invent items to fill a template. Empty sections are a valid result.
- Stay read-only until the user accepts changes. Don't edit tickets, files, or code on your own initiative. The only file this skill writes is the personal rules file, and only after the user says yes.
- Don't answer your own questions with assumptions, even plausible ones. Evidence goes in the evidence line, and the decision stays with the author.
