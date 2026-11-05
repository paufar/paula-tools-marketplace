# Team writing rules

These are rules about how to write, not about any subject. Each one names a kind of sentence and what it must always include. They're learned from Nitpicker reviews and shared with the team, and changed by PR. Personal rules learned on one machine live in `~/.claude/no-loose-ends/rules.md`, and the useful ones can be promoted here.

### Announcing a change
**When you write:** a sentence announcing a change: a rollout, launch, removal, migration, or deadline.
**Always include:** the exact date (with timezone if a time matters) and who it affects.
**Why:** "Next week" and "users" mean different things to every reader, so people prepare for the wrong day or don't realise it's about them.
**Before → after:** "The new dashboard rolls out next week." → "The new dashboard rolls out on 12 Nov 2026 to the beta group; everyone else gets it on 26 Nov."
**Applies to:** all
**Seen:** 1 (explainer example, 2026-11-04)

### Granting permission
**When you write:** a sentence that allows something: "is allowed", "can", "still works", "is accepted".
**Always include:** what makes it possible, or a note that this hasn't been confirmed yet.
**Why:** A permission stated without its basis may be impossible, and nobody finds out until someone tries it.
**Before → after:** "Saving is still allowed." → "Saving is still allowed (the duplicate check only warns; [confirm nothing else blocks it])."
**Applies to:** all
**Seen:** 1 (DAS-2516, 2026-11-04)

### Naming something the reader must find
**When you write:** the name of something the reader has to find or use: a file, setting, permission, page, document, or command.
**Always include:** its exact name as it appears at the source, and where to find it. If it doesn't exist yet, say so.
**Why:** A name written from memory looks right but matches nothing, and readers either search in vain or quietly substitute their own guess.
**Before → after:** "Requires the settings write permission." → "Requires `orders:manage` (defined in `rbac/permissions.ts`)."
**Applies to:** all
**Seen:** 1 (DAS-2516, 2026-11-04)

### Stating that something happens
**When you write:** a sentence saying something happens or is true: "is live", "is sent", "is available", "the screen says".
**Always include:** when it starts being true, if that's not immediately, and what's true until then.
**Why:** Readers take present tense literally and act on it before it's real.
**Before → after:** "After saving, the change is live within 5 minutes." → "Once the live-config switch is on, a saved change is live within 5 minutes. Until then, saving only stores it."
**Applies to:** all
**Seen:** 1 (DAS-2516, 2026-11-04)

### Describing how something is checked
**When you write:** how something will be tested, verified, reviewed, or proven.
**Always include:** where it's checked, and what result counts as passing.
**Why:** Without a place and a pass mark, every checker picks their own, and nobody can say when it's done.
**Before → after:** "Verify on a test environment." → "Verify on staging. It passes when the export shows the new value. Results from other environments don't count."
**Applies to:** all
**Seen:** 1 (DAS-2516, 2026-11-04)

### Recording a decision
**When you write:** that something was decided, agreed, or narrowed, or a section that lists decisions.
**Always include:** who decided and when, collected in one place. Write "none" only if it's true.
**Why:** Decisions scattered through the text get missed or reopened, and "none" next to a dated decision makes readers doubt both.
**Before → after:** "Decision: None." (with a decision dated 29 Sep further up) → "Decisions: live delay ~5 min (29 Sep, product owner)."
**Applies to:** all
**Seen:** 1 (DAS-2516, 2026-11-04)

### Using a soft verb
**When you write:** "may", "should", "could", "ideally", or "where possible" in anything someone must do or check.
**Always include:** a definite verb, or the exact options that are all acceptable.
**Why:** A soft verb hands the decision to the reader, and the next reader decides differently.
**Before → after:** "The address may be normalised." → "The address is saved lowercase." or "Either lowercase or as entered is accepted."
**Applies to:** all
**Seen:** 1 (DAS-2516, 2026-11-04)

### Leaving a placeholder
**When you write:** "TBD", "to confirm", "later", or any gap meant to be filled in.
**Always include:** who fills it and by when.
**Why:** A placeholder with no owner outlives the work it was for.
**Before → after:** "Files: to confirm." → "Files: [the implementer confirms before review]."
**Applies to:** all
**Seen:** 1 (DAS-2516, 2026-11-04)
