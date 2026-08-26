---
name: release
description: >
  Runs this repo's release gates, bumps independently versioned plugin
  manifests, re-validates, commits, and pushes. Use when the user asks to
  "release", "ship", "bump and push", "cut a release", or to bump a plugin
  version. For registering a plugin in the catalogue, use
  marketplace-and-release instead.
argument-hint: "[plugin-name] [patch|minor|major]"
---

# Release

End-to-end release workflow for **claude-for-financial-planners**. This is a
marketplace of independently versioned plugins, not a single-version package.
Run every command from the marketplace **repo root**.

**When invoked with arguments**, treat the first as the plugin to bump and the
second as the semver component. If either is missing, infer from the diff and
ask before bumping.

Do **not** register `plugin-management` in `.claude-plugin/marketplace.json`
unless the user explicitly overrides that.

If a changed **practice** plugin has no entry in
`.claude-plugin/marketplace.json`, load `marketplace-and-release` and register
it first (with confirmation). Then continue this skill. Skip that hand-off for
`plugin-management`.

## Workflow

### 1. Pre-flight checks

Run the gates from `AGENTS.md`. Python checks can run in parallel;
`claude plugin validate` only if the Claude CLI is on `PATH` — skip it and say
so if it isn't, rather than failing the release.

```bash
# Marketplace + per-plugin schema (skip if `claude` is not installed)
claude plugin validate .claude-plugin/marketplace.json
for d in plugins/*/; do
  [ -f "$d/.claude-plugin/plugin.json" ] || continue
  claude plugin validate "$d"
done

# JSON sanity
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"

# advice-core reference mirrors
python3 scripts/sync-references.py --check

# marketplace ↔ plugin.json field sync (name, description, author)
python3 scripts/check-marketplace-sync.py --check

# skill frontmatter, permission tiers, required headings
python3 scripts/validate-skills.py --check

# connector placeholder taxonomy
python3 scripts/validate-connectors.py --check
```

There is no `scripts/validate.py` and no test suite. **Stop if any gate fails.**
If `sync-references.py --check` fails because canonical
`plugins/advice-core/references/` files were edited, run
`python3 scripts/sync-references.py --apply` and re-check — do not leave mirrors
stale.

### 2. Determine version bump

Identify which plugin(s) under `plugins/` changed. Ask which semver component
to bump if not specified:

| Bump | When |
|------|------|
| patch | Bug fixes, prompt/content tweaks, docs |
| minor | New skills, new agents, new features |
| major | Breaking changes to a plugin, command, or skill map |

Default to **patch** if the user says "release" without specifying.

A **brand-new plugin's first release** is `0.1.0` — that is not a bump.

**0.x exception:** a pre-1.0.0 plugin whose README still describes it as
early-stage takes a **minor** bump for skill-map breakage (removed or renamed
skills), not major. Once a plugin reaches 1.0.0, the same change is major.

Bump only plugins that actually changed. Do not bump untouched catalogue
plugins. Bump `plugin-management` only when its own files changed.

### 3. Bump version

For each changed **practice** plugin, update `version` in:

- `plugins/<plugin>/.claude-plugin/plugin.json`

No plugin in this repo has a `.cursor-plugin/plugin.json` — do not add one.

For **plugin-management** (this toolkit), update `version` in:

- `plugins/plugin-management/.claude-plugin/plugin.json`

Do **not** bump `.claude-plugin/marketplace.json`'s `version` for a plugin
content release. Bump that field only when catalogue-level metadata itself
changes (adding/removing a listed plugin, changing the marketplace
description) and the user wants it.

`marketplace.json` does not carry per-plugin versions. After a description
change, `check-marketplace-sync.py` still requires `name` / `description` /
`author` to match the plugin manifest — keep those fields identical; the
version bump lives only in `plugin.json`.

### 4. Re-validate

Re-run the gates from step 1 (at least the Python checks, plus
`claude plugin validate` if available). Confirms the bump didn't introduce
JSON errors, marketplace drift, or stale reference mirrors.

### 5. Stage, commit, and push

Stage **only** the files this release touched — not `git add -A`.

```bash
git add <touched files>
git commit -m "<type>(<scope>): <summary>"
```

Commit message style: Conventional Commits (`feat(scope): …`, `fix(scope): …`,
`docs(scope): …`, `chore(scope): …`) — see `git log` for examples. Mention the
version bump in the summary or body, e.g. `feat(financial-adviser): add
annual-review-pack; bump financial-adviser to 0.2.0`.

⚠ Pushing to a shared branch is not fully reversible once others have pulled
it. **Require explicit user confirmation** before `git push`.

## Version source of truth

There is no single version file:

- Each plugin's version lives in `plugins/<plugin>/.claude-plugin/plugin.json`.
- `.claude-plugin/marketplace.json` is the catalogue, not a plugin version.

## Getting the update to users

Installed plugins do not always auto-refresh. After a bump, tell the user they
may need `/plugin update <name>@claude-for-financial-planners` (or a reinstall)
on each host. A brand-new catalogue plugin also needs the marketplace added
or refreshed before others can install it.

## Checklist (copy into your reasoning)

- [ ] practice plugins that are new to the catalogue went through `marketplace-and-release` first
- [ ] AGENTS.md gates pass (Claude CLI skipped only if missing)
- [ ] reference mirrors applied if canonical refs changed
- [ ] affected plugin versions bumped; no plugin has a Cursor manifest
- [ ] gates pass after the bump
- [ ] commit includes only this release's files
- [ ] user confirmed before push

## Related skills

- **`marketplace-and-release`** — catalogue registration (add an entry). After
  a confirmed register, hand off to this skill for version/commit/push.
- **`create-plugin`** — Phase 7 registers, then this skill ships.
