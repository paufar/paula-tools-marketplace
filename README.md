# AI Project Foundation

This is my AI project foundation. I copy it into a new project during
initialization so that every coding agent session starts from the same
documented system, instead of from a blank prompt.

It is a set of blank templates, not an application. Nothing here runs.
You fill the templates in for a specific project, and from then on the
agent reads them at the start of every session.

## How I use it

Install the plugins (see "Installing the plugins" below), open Claude
Code in the project, new or existing, and run the
`/project-foundation:init-project` skill. It does everything below and helps fill in
every section by asking how I want to complete it:

1. Copies the contents of `templates/` into the project root. Only
   that folder's contents are copied: the root `AGENTS.md`,
   `CLAUDE.md` are for maintaining this repo and stay here.
2. Adds `local-docs/` to `.gitignore`.
3. Fills in the context files, starting with `context/PROJECT.md`,
   by discussing each section with me, one question at a time.
4. Fills in `AGENTS.md`, replaces the `make check` stub in `Makefile`,
   and writes the build plan and first spec in `context/specs/`.
5. Fills in `local-docs/` and checks nothing was left as a placeholder.

For an existing project, the skill first reads every markdown file
already in it. Anything useful for a template is shown to me during
the fill-in, labelled with the file it came from, and I choose to use,
edit or replace it. Once absorbed, the old files are deleted after I
confirm. Files that serve other readers (README, LICENSE, CHANGELOG,
API docs) are kept by default.

While it runs, the skill keeps a `project-initialization.md` tracker
in the project root: created at the start, updated at every step and
every file, and deleted at the end. If a run is interrupted, the
tracker stays. Run `/init-project resume` in the project to pick up
where it stopped, or plain `/init-project` to be asked whether to
resume or start over.

Then the first session starts: the agent clocks in from
`context/PROGRESS.md` and clocks out by updating it.

The skill lives in this repo, in `plugins/project-foundation/skills/init-project/`
(`SKILL.md`, `SECTIONS.md`, `EXISTING.md`), so it is available in every
project once the plugin is installed. It reads the templates from the
plugin's own `templates/` folder, set at the top of its `SKILL.md` as
`${CLAUDE_PLUGIN_ROOT}/templates`. When a template changes, the skill's
files are updated in the same commit.

The skill also asks about `local-docs/goal.md`: what I want to get out
of the project for myself, such as learning a skill or a tool. That file
is private and never committed. The skill turns only the parts I clear
into guidance for agents in a committed file
(`context/AI-WORKFLOW-RULES.md`).

A second skill, `/project-foundation:test-me`
(`plugins/project-foundation/skills/test-me/`), closes
the loop. It reads `local-docs/goal.md`, interviews me on each goal,
grills my understanding using the real project, and judges whether the
goal was reached: Reached, Partly, Not yet, or Not tested. With my OK it
records the result and next steps in `goal.md`'s Notes, and nowhere else.

A third skill, `/learning-tools:interview-prep`
(`plugins/learning-tools/skills/interview-prep/`), works on any repo, template-based or not. Before an interview I run it with
the vacancy (a URL, a file, or pasted text; optional). It reads the project's
docs, dependencies, code and history, then briefs me on the architecture
decisions and the tools used and why, marking anything whose reason is not
recorded. If `local-docs/goal.md` exists it reads it too, so it knows where
I was shaky to begin with. It then mock-interviews me one question at a
time, weighted towards what the vacancy asks for and those weak spots, and
ends with a debrief: strong answers, shaky ones, and stories to have ready.
With my OK it saves the notes to `local-docs/interview-notes.md`, which is
gitignored, so nothing reaches a committed file. The skill checks with
`git check-ignore` before writing, refuses if the path is not ignored or is
already tracked, and never stages or commits, even if asked.

A fourth skill, `/learning-tools:close-session`
(`plugins/learning-tools/skills/close-session/`), closes off any
session, whether or not it was about the project. It writes a detailed
`tmp/SESSION_SUMMARY.md` (creating `tmp/` if needed): what the session was
about, what happened, the state right now, dead ends, open questions, a
checklist of open items and to-dos (even ones not yet project tasks) and the
next steps. Earlier summaries are kept, newest first. It is separate from
`PROGRESS.md`, which records the project only, and it never edits that file.
It never stages or commits, and warns if `tmp/` is not gitignored.

## Installing the plugins

This repo is a Claude Code plugin marketplace named `paula-tools`, with
three plugins:

| Plugin | Skills |
| ------ | ------ |
| `project-foundation` | `/project-foundation:init-project`, `/project-foundation:test-me`, and the `templates/` they use |
| `learning-tools` | `/learning-tools:interview-prep`, `/learning-tools:close-session` |
| `nitpicker` | `/nitpicker:nitpicker`, `/nitpicker:no-loose-ends` |

In Claude Code, add the marketplace once, then install the plugins:

```
/plugin marketplace add paufar/paula-tools-marketplace
/plugin install project-foundation@paula-tools
/plugin install learning-tools@paula-tools
/plugin install nitpicker@paula-tools
```

To try it from a local clone instead, use
`/plugin marketplace add ~/Work/paula-tools-marketplace`. After the repo
changes, run `/plugin marketplace update paula-tools` to pick it up.

The repo is the only copy of these skills. Do not also keep them in
`~/.claude/skills/`, or each skill will show up twice.

## How to use the skills

| When | Run | What happens |
| ---- | --- | ------------ |
| Starting a project, new or existing | `/project-foundation:init-project` | Copies the templates into the project and fills them in with you. `/project-foundation:init-project resume` picks up an interrupted run |
| Later, to check you reached your own goals | `/project-foundation:test-me` | Interviews you on `local-docs/goal.md` and judges each goal |
| Before an interview, in any repo | `/learning-tools:interview-prep <vacancy URL, file or text>` | Briefs you on the repo, then mock-interviews you. The vacancy is optional |
| At the end of any session | `/learning-tools:close-session [focus]` | Writes `tmp/SESSION_SUMMARY.md` so the next session can resume |
| Before handing a ticket, plan or article to others | `/nitpicker:nitpicker <text, file, ticket ID or URL>` | Lists every decision the reader would have to guess, ranked. See `plugins/nitpicker/README.md` |
| Writing a ticket, spec or doc | `/nitpicker:no-loose-ends` | Drafts it with the saved writing rules applied |

Typical flow for a new project:

1. Open Claude Code in the project folder.
2. Run `/project-foundation:init-project` and answer its questions, one
   at a time.
3. Work as usual. Each session the agent clocks in from
   `context/PROGRESS.md` and clocks out by updating it.
4. Run `/learning-tools:close-session` when you stop, for a hand-off note.
5. When the project is done, run `/project-foundation:test-me`, and
   `/learning-tools:interview-prep` before an interview about it.

The first four skills are user-invoked only: the agent never runs them on its own.

## What is in `templates/`

`templates/` is `plugins/project-foundation/templates/`.

| File | Committed | Purpose |
| ---- | --------- | ------- |
| `AGENTS.md` | yes | Entry point every agent reads first |
| `CLAUDE.md` | yes | Pointer so Claude Code reads `AGENTS.md` |
| `Makefile` | yes | `make check`, the single consistency command |
| `context/*.md` | yes | Seven context docs: project, architecture, UI, standards, workflow rules, progress, decisions |
| `local-docs/goal.md` | no, gitignored, private | What I want to achieve for myself alongside the project. Only cleared parts reach committed files |
| `local-docs/setup.md` | no, gitignored | Detailed setup reference for humans |
| `local-docs/architecture.html` | no, gitignored | Illustrated reference, including every package, plugin and tool and why it is used |

Rules that apply to every template:

- Each file stays between 100 and 150 lines once filled in. Detail
  moves to a linked doc instead of growing the file.
- `local-docs/` is gitignored, so `AGENTS.md` does not reference it.

Rule for maintaining this repo: any time a template changes,
update `foundation-overview.html` and every other affected file in
the same change. The full checklist is in the root `AGENTS.md`.

There are two `AGENTS.md` files. The root one is for agents
maintaining this repo and is never copied. `templates/AGENTS.md`
is the project entry point and is copied into every new project.

[foundation-overview.html](foundation-overview.html) explains the
setup and why each file exists.

## Repo layout

```
📁 paula-tools-marketplace/
├── README.md                    ← This file
├── foundation-overview.html     ← Why each file exists
├── AGENTS.md, CLAUDE.md         ← Rules for maintaining this repo (not copied)
├── .claude-plugin/marketplace.json ← The paula-tools marketplace (not copied)
└── plugins/
    ├── learning-tools/          ← Plugin: interview-prep and close-session skills (not copied)
    │   ├── .claude-plugin/plugin.json
    │   └── skills/{interview-prep,close-session}/SKILL.md
    ├── nitpicker/               ← Plugin: nitpicker and no-loose-ends skills (not copied)
    │   ├── .claude-plugin/plugin.json
    │   ├── README.md, docs/explainer.html
    │   └── skills/{nitpicker,no-loose-ends}/
    └── project-foundation/      ← Plugin: init-project and test-me skills + templates (not copied)
        ├── .claude-plugin/plugin.json
        ├── skills/init-project/ ← SKILL.md, SECTIONS.md, EXISTING.md
        ├── skills/test-me/SKILL.md
        └── templates/           ← Copy the contents of this folder into a project
            ├── AGENTS.md        ← Entry point: overview, stack, constraints, clock in/out
            ├── CLAUDE.md        ← One-line pointer to AGENTS.md
            ├── Makefile         ← `make check` stub used by clock in/out
            ├── context/
            │   ├── PROJECT.md           ← Blank template
            │   ├── ARCHITECTURE.md      ← Blank template
            │   ├── CODING-STANDARDS.md  ← Blank template
            │   ├── AI-WORKFLOW-RULES.md ← Blank template
            │   ├── UI-CONTEXT.md        ← Blank template
            │   ├── PROGRESS.md          ← Task tracker with a "Done when" per item
            │   └── DECISIONS.md         ← Decision log
            └── local-docs/
                ├── goal.md              ← Private personal goals (gitignored)
                ├── setup.md             ← Detailed setup reference (gitignored)
                └── architecture.html    ← Architecture + every package/tool and why (gitignored)
```
