# Plugin Management

Create, customize, validate, register, and release plugins for **this repo**. Advisers and brokers should not install this. It is **not** in `.claude-plugin/marketplace.json` — load it from the directory.

Adapted from Temple & Webster's `plugin-management` plugin (Apache-2.0). Conventions below are this marketplace's: `plugins/<name>/`, a single Claude Code / Cowork catalogue, and the licensed-human trust spine in `AGENTS.md`.

## Load it

From the repo root, in Claude Code:

```bash
claude plugin install ./plugins/plugin-management
```

Or in a Cowork/Code session, install from the `plugins/plugin-management` folder (not via `/plugin install …@claude-for-financial-planners` — that catalogue will not list it). Restart after install.

**Do not** add a `.cursor-plugin/` manifest or marketplace to this repo unless the project decides to ship a dual catalogue. Plugins here — including this toolkit — get `.claude-plugin/plugin.json` only.

## What it does

| Skill / agent | Role |
|---|---|
| `create-plugin` | Guided new plugin, confirmation before writes, confirmation before catalogue registration |
| `customize-plugin` | Adapt an existing plugin |
| `plugin-structure` | Directory + manifest shape **for this repo** |
| `skill-development` / `agent-development` / `hook-development` / `mcp-integration` / `plugin-settings` / `plugin-portability` / `command-development` | Component authoring |
| `marketplace-and-release` | Register a **practice** plugin in the catalogue — never this plugin itself unless the user explicitly asks |
| `release` | Run AGENTS.md gates, bump plugin versions, commit, and push |
| `plugin-scaffolder` | Only writer agent |
| `plugin-validator` / `skill-reviewer` / `component-recommender` | Read-only |

## This repo's rules (do not inherit T&W defaults)

- Plugins live at `plugins/<name>/`.
- Catalogue is **single**: `.claude-plugin/marketplace.json`. `source` is `./plugins/<name>`. Category is `productivity` unless a closer existing entry exists.
- New plugins match `advice-core` (practice profile `CLAUDE.md`, `practice-setup`, trust spine). Do not scaffold `.cursor-plugin/` for practice plugins.
- After scaffold, run the validators in [AGENTS.md](../../AGENTS.md). This repo has no `scripts/validate.py` — use the `release` skill (or `scripts/check-marketplace-sync.py`, `validate-skills.py`, `validate-connectors.py`, `sync-references.py`, and `claude plugin validate` by hand).
- Catalogue skills (the four practice plugins) need `metadata.work_shape`, `## Outputs`, `## Worked example`, and `## Propose profile update` except `practice-setup`. This toolkit's own skills do not — they are not in the catalogue and `validate-skills.py` does not scan them.
- **Never register `plugin-management` in `marketplace.json`** unless the user explicitly overrides that.

## Quickstart

> "Create a plugin for paraplanners that drafts FDS packs"

Walk `create-plugin`. Stop before Phase 7 until they confirm they want a catalogue entry.

> "Release the financial-adviser plugin"

Use `release`. Confirm the bump type if not given; confirm before push.
