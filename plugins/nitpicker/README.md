# nitpicker

Two skills that work as a pair. `nitpicker` reads a ticket, plan or article as a smart newcomer would and lists every decision the reader would have to guess. `no-loose-ends` writes the next one with the lessons applied.

```
/plugin install nitpicker@paula-tools
```

## nitpicker: review

```
/nitpicker:nitpicker [ticket | text | report] [--blocking-only] <text | file | DAS-1234 | URL>
```

You can also just ask: "nitpick DAS-1234", "is this ticket ready for devs?", "tighten this article".

| Mode | Picked automatically for | Output |
|---|---|---|
| `ticket` | Linear IDs, work items | Questions for the author (must answer / worth answering), plus recommendations to add to the ticket |
| `text` | Articles, docs, announcements, emails | An interactive page: each snippet with a suggested change and an accept checkbox, a live preview of the revised text, and copy/download |
| `report` | Plans and specs tied to a repo | A full ranked review with evidence and locations, plus a list of checked references |

Questions are ranked **blocking** (a wrong guess changes the work) or **non-blocking** (cheap to fix in review). It never edits tickets or posts comments unless you ask.

## Writing rules

Each review ends with **rules for next time**. These are rules about writing, not about the subject. Each names a kind of sentence and what it must always include, for example: *When you announce a change, always include the exact date and who it affects.* They're saved only if you say yes.

| File | What it holds |
|---|---|
| `skills/no-loose-ends/references/rules.md` | **Team rules.** Change them by PR. |
| `~/.claude/no-loose-ends/rules.md` | **Personal rules**, learned on your machine. |

```
/nitpicker:nitpicker rules                    list rules, Seen counts, rules ready for the team
/nitpicker:nitpicker rules show <title>       one rule in full
/nitpicker:nitpicker rules promote --ready    draft a PR adding rules seen 3+ times to the team file
/nitpicker:nitpicker rules remove <title>     delete a personal rule, or propose removing a team rule
```

The first time you run `promote`, it asks for the path of your local clone of this repo.

## no-loose-ends: write

"Write a ticket for…", "turn these notes into a ticket", or `/nitpicker:no-loose-ends`. It loads both rule files, looks up names in the repo before writing them down, copies the structure of recent tickets from your team, and lists open questions instead of guessing. It only creates a Linear ticket if you ask.

## Needs

- **A Linear connection in Claude Code** to read tickets by ID, for example through Anthropic's `engineering` plugin on claude.ai. Turn it on if you haven't, and sign in to Linear once. Without a connection, paste the ticket text instead.
- **`python3`** for the `text` mode page.
- **Run it from a folder containing the repo** the ticket is about, so it can check names against the code.

A full explainer page is in [`docs/explainer.html`](docs/explainer.html).
