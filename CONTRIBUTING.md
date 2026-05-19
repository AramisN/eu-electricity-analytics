# Contributing / Development Workflow

This is a solo project, but the workflow follows team conventions so the
repository looks professional and the habit transfers to client work.

## Branch model

- `main` is protected. Never commit directly.
- All work happens in **feature branches**, opened via Pull Request, and merged into `main`.
- One branch = one logical change. Don't bundle unrelated work.

### Branch naming

```
feat/<short-description>      # new feature
fix/<short-description>       # bug fix
chore/<short-description>     # tooling, deps, config
docs/<short-description>      # documentation
refactor/<short-description>  # code cleanup, no behavior change
```

Examples: `feat/entsoe-ingestion`, `chore/setup-pre-commit`, `docs/architecture-diagram`.

## Commit messages — Conventional Commits

Format:

```
<type>(<scope>): <short summary>

<optional body>

<optional footer>
```

**Types**: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `perf`, `build`, `ci`.

Examples:

```
feat(ingestion): add ENTSO-E day-ahead price endpoint client
fix(dbt): handle DST transition days in fct_prices_hourly
docs(adr): add ADR-003 explaining Iceberg over plain Parquet
chore(deps): bump ruff to 0.5.0
```

This isn't pedantry — it makes `git log` readable in 6 months and is the
default style at every serious data team in 2026.

## Pull Request workflow (even solo)

1. Branch off `main`: `git checkout -b feat/some-thing`
2. Make atomic commits as you work.
3. Push: `git push -u origin feat/some-thing`
4. Open a PR on GitHub against `main`.
5. Wait for CI to pass (lint + tests).
6. **Read your own diff** as if you were a reviewer. Leave a self-comment on anything you'd flag.
7. Merge using **Squash and merge** (keeps `main` history clean) or **Rebase and merge** if you want individual commits.
8. Delete the feature branch on GitHub after merging.
9. Locally: `git checkout main && git pull && git branch -d feat/some-thing`

This habit is worth practising even alone — it's the workflow every client expects.

## Resolving merge conflicts

When you eventually hit one:

```bash
git checkout main
git pull
git checkout feat/your-branch
git rebase main           # replay your commits on top of latest main
# resolve any conflicts in editor; mark with `git add <file>`
git rebase --continue
git push --force-with-lease  # safe force; rejects if remote moved
```

If a rebase goes wrong: `git rebase --abort` returns you to safety.

## Pre-commit hooks

Installed once with `pre-commit install`. After that, every `git commit` runs:

- `ruff` lint + format (auto-fixes most issues)
- `mypy` type check
- Trailing whitespace, end-of-file, YAML/JSON/TOML validation
- Secret detection (catches API keys before they're committed)
- Conventional commit message format check

If a hook fails, the commit is rejected. Fix the issue and re-commit.

To bypass in emergencies: `git commit --no-verify` (don't make a habit of it).

## Releases

Use **Git tags** + GitHub Releases for milestones:

```bash
git tag -a v0.1.0 -m "Q1 milestone: full pipeline working end-to-end"
git push origin v0.1.0
```

Then on GitHub: Releases → Draft a new release → pick the tag → write notes.

## Local development

See [README.md → Quickstart](README.md#quickstart-local-development).

## Architecture Decisions

Every significant choice goes in [`docs/decisions/`](docs/decisions/) as an
ADR (Architecture Decision Record). Template: copy `000-using-adrs.md`
and modify. Number sequentially.
