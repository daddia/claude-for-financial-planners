---
name: plugin-structure
description: Explains how a plugin directory is laid out for this marketplace — plugins/<name>/, a single .claude-plugin/plugin.json, the plugin-root rule, marketplace category, and when a bare SKILL.md is enough versus skills/<name>/. Use when the user asks to "create a plugin", "scaffold a plugin", "add a plugin to the marketplace", "where does plugin.json go", or is starting a new plugins/<name>/ directory from scratch.
---

# Plugin structure

A plugin here is a directory under `plugins/<name>/`. This skill covers the shape of
that directory and its manifest in full — everything needed to scaffold a correct
plugin without leaving this file.

**This repo (`claude-for-financial-planners`)** ships to Claude Code / Cowork with a
**single** catalogue (`.claude-plugin/marketplace.json`). Practice plugins get
`.claude-plugin/plugin.json` only — do **not** add `.cursor-plugin/` or a second
marketplace file unless the user has decided to dual-host the whole catalogue.
This toolkit follows the same rule.

Match an existing sibling (`advice-core`) rather than inventing layout.

## Manifest

```
plugins/<name>/
└── .claude-plugin/
    └── plugin.json     # Claude Code / Cowork
```

Minimum required fields: `name`, `description`, `version`, `author`. `name` must
equal the plugin's folder name exactly. Author for first-party plugins:

```json
{
  "name": "my-plugin",
  "displayName": "My Plugin",
  "description": "One sentence a marketplace browser can act on.",
  "version": "0.1.0",
  "author": {
    "name": "Jonathan Daddia",
    "url": "https://github.com/daddia"
  }
}
```

There is no repo-wide version — each plugin versions independently. See
`marketplace-and-release`.

If you are working in a *different* repo that already pairs `.cursor-plugin/`
manifests, match that repo — do not strip a pairing it already maintains.

## The plugin-root rule

Only `plugin.json` lives inside `.claude-plugin/`. Every other component —
`skills/`, `commands/`, `agents/`, `hooks/`, `.mcp.json`, `CLAUDE.md`, `README.md`,
`references/` — sits at the **plugin root**, never nested inside the manifest folder:

```
plugins/my-plugin/
├── .claude-plugin/plugin.json
├── CLAUDE.md             # practice-profile TEMPLATE (catalogue plugins)
├── README.md
├── CONNECTORS.md         # optional
├── skills/
│   └── some-skill/SKILL.md
├── agents/
│   └── some-agent.md     # scheduled watchers only
├── hooks/hooks.json      # empty stub is fine
├── references/
├── .mcp.json             # optional
└── ...
```

Getting this backwards (e.g. `.claude-plugin/skills/...`) is the single most common
scaffolding mistake — the component simply won't be discovered by either host.

## Skills are the primary component

Default to `skills/` for everything a plugin does — both agent-invoked guidance
("teach me how to do X") and user-invoked procedures (a person explicitly runs it by
name, the way a slash command works). A skill can carry `argument-hint` and a
tool-scoping field in its frontmatter for the user-invoked case, same file, same
directory shape, no separate component type required.

`commands/*.md` is a **legacy** layout, covered fully in the `command-development`
skill — reach for it only when a host or an existing plugin already depends on that
file shape, not for new work.

## Bare `SKILL.md` vs a full `skills/<name>/` directory

Both are valid; the choice is about whether the skill needs bundled resources, not
about the skill's importance.

| Shape | When |
| :---- | :--- |
| `skills/<name>/SKILL.md` only | The skill is self-contained guidance or a short procedure. No bundled files. This is the common case. |
| `skills/<name>/SKILL.md` + `references/`, `prompts/`, `agents/`, `examples/` | The skill has enough depth that inlining everything would bloat the body every time it triggers, or it needs skill-specific sub-agents/knowledge that no other skill shares. |

See the `skill-development` skill — and this plugin's own `skills/skill-development/`
directory as a live example — for how to decide and how to keep `SKILL.md` a thin
router once it grows resources.

## Illustrating a component vs shipping one

When a skill bundles a worked example of *another* skill, agent, or command (for
teaching purposes, the way this plugin's own `skill-development` skill does), never
name that illustration file `SKILL.md`, put it directly under `agents/*.md`, or put it
directly under `commands/*.md`. Those are the exact filenames/locations hosts use for
auto-discovery — some scan recursively, so even nesting one inside a skill's own
`examples/` directory can cause it to be picked up as a real, installable component.
Show the illustration as a fenced code block inside an ordinary `.md` file instead
(e.g. `examples/worked-example.md` containing a ```` ```markdown ```` block), never as
a file a host would discover on its own.

## The `category` field

`category` lives on the **marketplace manifest entry** for this plugin, not on the
plugin's own `plugin.json`:

```json
{
  "name": "my-plugin",
  "description": "…",
  "source": "./plugins/my-plugin",
  "category": "productivity",
  "author": {
    "name": "Jonathan Daddia",
    "url": "https://github.com/daddia"
  }
}
```

This repo's catalogue is **only** `.claude-plugin/marketplace.json`. `name`,
`description`, and `author` must match the plugin's `plugin.json`
(`scripts/check-marketplace-sync.py`). Category is `productivity` to match existing
entries. Do **not** register `plugin-management` unless the user explicitly asks.
See `marketplace-and-release`.

## Optional: a plugin-level `settings.json`

A plugin can declare a default sub-agent or other plugin-wide configuration via a
`settings.json` at the plugin root. Add it only when a concrete need shows up (a
default agent, a plugin-scoped setting) — don't add it speculatively. Keep it at the
plugin root alongside `README.md`, following the same plugin-root rule as everything
else above.

Don't confuse this with **per-project, user-editable configuration** — a plugin that
needs a file a user fills in once installed, that hooks/skills read back at runtime.
That's a different, unrelated pattern; see the `plugin-settings` skill.

## Checklist for a new plugin directory

- [ ] `plugins/<name>/.claude-plugin/plugin.json` (`name` matches the folder)
- [ ] Catalogue plugins: `CLAUDE.md` practice-profile template + `practice-setup` skill
- [ ] At least one component (`skills/` preferred) at the plugin root
- [ ] Non-empty `README.md`
- [ ] `claude plugin validate ./plugins/<name>` and the Python checks in `AGENTS.md`

## Related skills

- **`skill-development`** — authoring the `SKILL.md` files themselves; the default,
  primary component type.
- **`command-development`** — the legacy `commands/*.md` layout and its section
  conventions, for cases that still need it.
- **`agent-development`** — the `agents/*.md` format and tool scoping.
- **`plugin-settings`** — per-project, user-editable configuration, a different
  concept from this skill's plugin-root `settings.json`.
- **`marketplace-and-release`** — registering the finished plugin and shipping it.
