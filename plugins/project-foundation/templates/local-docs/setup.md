# Setup Guide

> Keep this file to 100 - 150 lines once filled in. Move detail into a linked doc rather than growing it.

Detailed reference for getting **[Project name]** running from a clean
machine. This is for humans and for agents that hit a setup problem.
The short version lives in `AGENTS.md` under "First-Run Commands".

Keep this file accurate. When a setup step changes, update it in the
same change.

## 1. Prerequisites

| Tool | Required version | How to check | Install |
| ---- | ---------------- | ------------ | ------- |
| [Node.js] | [22.x] | `node -v` | [nvm install 22] |
| [Package manager] | [npm 10.x] | `npm -v` | [bundled with Node] |
| [Database] | [PostgreSQL 16] | `psql --version` | [brew install postgresql@16] |
| [Git] | [2.40+] | `git --version` | [brew install git] |
| make | any | `make -v` | [preinstalled on macOS/Linux] |

Accounts and services needed:

- [e.g. Clerk account, with a dev application created]
- [e.g. Database host (local, Supabase, Neon)]
- [e.g. Blob storage bucket]

## 2. Get the code

```bash
git clone [repo url]
cd [project folder]
```

## 3. Environment variables

Copy the template and fill in each value:

```bash
cp .env.example .env.local
```

| Variable | Required | Where to get it | Example / format |
| -------- | -------- | --------------- | ---------------- |
| `[DATABASE_URL]` | yes | [database provider dashboard] | `postgresql://user:pass@localhost:5432/dbname` |
| `[AUTH_SECRET_KEY]` | yes | [auth provider dashboard, API keys] | `sk_test_...` |
| `[AUTH_PUBLIC_KEY]` | yes | [same page] | `pk_test_...` |
| `[OTHER_VAR]` | [no] | [where] | [format] |

Rules:

- Never commit `.env.local`. Only `.env.example` (no real values) is committed.
- Variables prefixed `[NEXT_PUBLIC_]` ship to the browser. Never put secrets in them.

## 4. Install dependencies

```bash
[npm install]
```

Expected: completes with no errors; `node_modules/` exists.

## 5. Database setup

```bash
[npm run db:migrate]   # apply migrations
[npm run db:seed]      # optional: load sample data
```

Expected: [tables X, Y, Z exist; check with `npm run db:studio`].

To reset the local database (local only, this destroys data):

```bash
[npm run db:reset]
```

## 6. Run the app

```bash
[npm run dev]
```

Expected: [server listens on http://localhost:3000; the home page
loads without console errors].

## 7. Verify the setup

```bash
make check
```

Expected: exits 0. This runs [lint, type-check, tests, build]. If it
fails on a fresh clone, the setup is incomplete. Do not start feature
work until it passes.

## 8. Everyday commands

| Command | What it does |
| ------- | ------------ |
| `[npm run dev]` | Start the dev server |
| `[npm run build]` | Production build |
| `[npm run lint]` | Lint |
| `[npm run typecheck]` | Type-check |
| `[npm test]` | Run tests |
| `make check` | Lint + types + tests + build; must pass before committing |

## 9. Project layout

Short map only. Boundaries and rules are in `context/ARCHITECTURE.md`.

```
[project]/
├── AGENTS.md          # agent entry point
├── context/           # the context docs (PROJECT, ARCHITECTURE, PROGRESS, ...)
├── local-docs/        # this file, the architecture reference, goal.md (all gitignored)
├── [src/ or app/]     # [application code]
└── Makefile           # `make check`
```

## 10. Deployment

- **Target:** [e.g. Vercel]
- **Build command:** [npm run build]
- **Environment variables to set in the host:** [same as section 3, production values]
- **Migrations:** [how and when they run in production]
- **Rollback:** [how to roll back a bad deploy]

## 11. Troubleshooting

| Symptom | Likely cause | Fix |
| ------- | ------------ | --- |
| [`Cannot connect to database`] | [DB not running, or wrong `DATABASE_URL`] | [start the DB; recheck the URL] |
| [Auth redirects in a loop] | [Missing or wrong auth keys] | [recheck section 3] |
| [Port 3000 in use] | [Another process] | [`lsof -i :3000`, stop it, or set `PORT`] |
| [`make check` fails on fresh clone] | [Skipped a setup step] | [redo sections 3 to 5 in order] |

## 12. Change log for this guide

- [YYYY-MM-DD] Initial version.
