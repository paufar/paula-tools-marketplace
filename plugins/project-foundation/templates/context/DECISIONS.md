# Decisions

> Keep this file to 100 - 150 lines. Condense or drop superseded entries as it grows.

## Decision definition

**Date:** [dd-mm-yyyy]
**Decision:** [Leave "Exposed schemas" empty on both projects, which the dashboard reports as the Data API being disabled. When a table is ready (RLS policies in place), expose that specific table, not the whole `public` schema.]

**Reasoning:** [There's no separate "Data API on/off" toggle plus an "auto-expose new tables" sub-setting as originally assumed — it's one selector for schemas or individual tables, and an empty selection just turns the API off. An empty selection is the strictest version of "nothing reachable by default," and exposing per-table instead of per-schema is a tighter gate than the schema-level one first planned, so RLS isn't the only thing standing between the `anon` key (which ships to the browser) and a table going live.]

**Supersedes:** [an earlier version of this decision that said to keep the Data API "enabled but with auto-expose off" — that setting doesn't exist in the dashboard.]