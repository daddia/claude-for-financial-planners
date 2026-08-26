# AGENTS.md

Guidance for working on this repo. `claude-for-financial-planners` is a Claude Code / Cowork plugin marketplace — four first-party plugins for Australian financial advisers and mortgage brokers. Most work here is editing prompt content (skills), plugin metadata, or reference material — not application code.

## Layout

```
.claude-plugin/marketplace.json   # marketplace manifest — one entry per catalogue plugin
plugins/<name>/                   # catalogue plugins (advice-core, financial-adviser, mortgage-broker, compliance)
  .claude-plugin/plugin.json
  .mcp.json
  CLAUDE.md                       # practice-profile TEMPLATE (not runtime user data)
  README.md
  skills/<name>/SKILL.md
  references/
  agents/<name>.md                # scheduled watchers only
  hooks/hooks.json                # empty stub
plugins/plugin-management/        # maintainer toolkit — NOT in marketplace.json
plugins/references/               # shared mirror of advice-core setup refs + connector-taxonomy.json
                                  # (not a plugin — no plugin.json)
docs/                             # design briefs and contributor docs
managed-agents/                   # future cookbooks (agent.yaml + subagents/)
scripts/
```

## Validation — run before opening a PR

```bash
# 1. Marketplace + per-plugin schema (if Claude CLI is installed)
claude plugin validate .claude-plugin/marketplace.json
for d in plugins/*/; do
  [ -f "$d/.claude-plugin/plugin.json" ] || continue
  claude plugin validate "$d"
done

# 2. JSON sanity
python3 -c "import json,glob; [json.load(open(f)) for f in glob.glob('**/*.json', recursive=True)]"

# 3. advice-core reference mirrors
python3 scripts/sync-references.py --check

# 4. marketplace ↔ plugin.json field sync (name, description, author)
python3 scripts/check-marketplace-sync.py --check

# 5. skill frontmatter, permission tiers, required headings
python3 scripts/validate-skills.py --check

# 6. connector placeholder taxonomy
python3 scripts/validate-connectors.py --check
```

### Marketplace invariants (I1–I11)

Same conventions as `anthropics/claude-plugins-official`. Plugins array is in **curated display order** (advice-core first) — ask before alpha-sorting.

### Frontmatter requirements

These apply to **catalogue** plugins (the four entries in `marketplace.json`). `validate-skills.py` walks marketplace sources only — it does not scan `plugins/plugin-management/`.

Every catalogue `skills/<name>/SKILL.md` needs `description`. Multi-line descriptions use `>` block scalars.

Required headings: `## Outputs`, `## Worked example`. Every skill except `practice-setup` also needs `## Propose profile update`.

`metadata.work_shape` must be one of: `hypothesis-driven-analysis`, `option-evaluation`, `structured-aggregation`, `narrative-synthesis`, `governance-tracking`.

Permission tiers: `advisory` (`Read, Grep, Glob`) or `artefact-writer` (`Read, Grep, Glob, Write`) for `practice-setup`, `ai-governance-setup`, `audit-export`.

## Conventions

### Keep `marketplace.json` in sync with `plugin.json`

For first-party plugins, `marketplace.json`'s `name`, `description`, and `author` must match `plugins/<plugin>/.claude-plugin/plugin.json`.

### Plugin agents vs job-style names

`agents/<name>.md` files are scheduled/background watcher definitions only. Job-style on-demand agents are README labels that map to slash commands under `skills/` — do not add duplicate files under `agents/`.

### Skill names in prose must be canonical

When a `SKILL.md` tells the user "run `/foo`," `foo` must be the actual `skills/<foo>/` directory name.

### Plugin CLAUDE.md is a template, not project context

Each `plugins/<plugin>/CLAUDE.md` is a practice-profile template that `practice-setup` copies to `~/.claude/plugins/config/claude-for-financial-planners/<plugin>/CLAUDE.md`. Organisation-wide facts live once in `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md`. It is *not* loaded as project context when the plugin is installed — `claude plugin validate` may warn; don't "fix" it by moving the content into a skill.

**Living profile.** `practice-setup` is the only skill that auto-applies a full profile write (after confirmation). Every other skill must use **propose profile update**.

### Guardrail spine

This is a regulated domain. Skills must:

- Stamp **draft for licensed human review** — not personal advice, not credit assistance
- Never autonomously select a product/lender as a client recommendation
- Never finalise SOA/CAR/BID as signed
- Surface incomplete information (s961B / RG 273)
- Keep `soa-draft` **SOA-default**; CAR only when the licensee confirms (DBFO not fully settled)
- Not assume s961B(2) safe-harbour steps are removed
- Prefer `[verify]` on model-only policy/product facts

Canonical trust rules: `plugins/advice-core/references/trust-conventions.md`. After editing, run `python3 scripts/sync-references.py --apply`.

### `references/` ships with `advice-core`, mirrored at `plugins/references/`

Shared setup refs live in `plugins/advice-core/references/` so they ship with the core plugin. Other plugins carry copies. `plugins/references/` is the contributor/validator mirror (plus `connector-taxonomy.json` and `skill-design-framework.md`) — it is **not** an installable plugin. Skills cite refs plugin-relative (`../../references/<file>.md` from `skills/<name>/`).

### Formatting

- 2-space indent in JSON and `.mcp.json`
- Final newline at end of every text file
- No trailing whitespace

### Maintainer toolkit is not in the catalogue

`plugins/plugin-management/` is a local install for people who maintain this repo. Load it with `claude plugin install ./plugins/plugin-management` — never via `@claude-for-financial-planners`, and never add it to `marketplace.json` unless the user explicitly overrides that. New practice plugins get `.claude-plugin/plugin.json` only. `validate-connectors.py` skips this directory because its teaching examples use generic `~~` placeholders outside this marketplace's taxonomy.

## Release flow

Use the `release` skill (`plugins/plugin-management/skills/release/SKILL.md`) rather than doing this by hand — it runs the gates above, bumps the right `plugin.json` files, re-validates, and commits with Conventional Commits. Require confirmation before push.

## Things to leave alone

- `hooks/hooks.json` stubs are empty on purpose
- Do not add a first-party XPLAN/ApplyOnline MCP URL unless a vendor has shipped one
- Do not register `plugin-management` in the adviser/broker catalogue
