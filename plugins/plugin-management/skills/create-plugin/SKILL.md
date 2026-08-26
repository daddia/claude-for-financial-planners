---
name: create-plugin
description: Guided, multi-phase workflow to build a new plugin for this marketplace end to end — discovery, component planning, scaffold, component authoring, validation, local test, and marketplace registration. A thin orchestrator over this plugin's own component skills and agents. Use when the user asks to "create a plugin", "build a plugin", "make a new plugin", "scaffold a plugin", "start a plugin from scratch", or "add a plugin to the marketplace".
argument-hint: "[plugin name or a description of what it should do]"
---

# Create a plugin

Walk the user from an idea to a complete, validated, registered plugin. This skill is
a **thin orchestrator**: it doesn't restate how to write a skill, an agent, or a
manifest — it triggers the skill or agent that owns each phase, in order, and tracks
progress across them. Load each referenced skill at the phase that needs it rather
than reading everything up front.

**When invoked with an argument**, treat it as the plugin's name or a description of
its purpose and fold it into Phase 1.

## How to run it

Track progress across phases with a todo list where the host supports one. Phases 1–2
happen entirely in conversation — nothing is written to disk until the component plan
is confirmed. After each write-heavy phase, re-check the result rather than assuming
success.

Ask the user questions with a structured question prompt where the host supports one
(Cowork and Cursor both do); otherwise ask in plain prose. Keep user-facing
conversation in plain language — frame everything in terms of what the plugin will
*do*, not its file paths or schema fields, unless the user asks for that detail.

## Preflight

- **Repo.** Confirm you're in the repo that should hold the new plugin — this
  marketplace keeps plugins under `plugins/<name>/`. If unsure which repo or the user
  wants a standalone plugin to hand off rather than a marketplace entry, ask before
  writing anything.
- **Not this toolkit.** Do not register `plugin-management` in `marketplace.json`
  unless the user explicitly overrides that.
- **Name collision.** If a name was given, confirm `plugins/<name>/` doesn't already
  exist. If it does, this is an edit to an existing plugin (use `customize-plugin` or
  the individual component skills), not a new one.
- **Tooling for later phases.** For registration/release, confirm `git` is available;
  if this repo has a validator or test suite, confirm its runtime (`python3`, etc.) is
  on `PATH`. In Cowork, confirm you can reach the outputs directory if the user wants a
  packaged `.plugin` file at the end.

## Phase 1: Discovery

If the argument already states the purpose clearly, summarise it back and confirm.
Otherwise ask only what's unclear:

- What should this plugin do, and for whom? What problem does it solve?
- Which existing plugin in this marketplace is it closest to in shape or ownership?
- Does it integrate with any external tools or services?
- Is there an existing codebase or repo it needs to serve, separate from this
  marketplace repo itself? If so, note its path — Phase 2 scans it for
  recommendations rather than guessing from the description alone.
- Does it need to run on hosts beyond the one you're using now (Claude Cowork,
  Cursor)? The `plugin-portability` discipline applies either way, but the answer
  changes how much you flag host-specific choices as you go.

Confirm the purpose before proceeding.

## Phase 2: Component planning

Load the `plugin-structure` skill to ground the options.

**If the plugin serves an existing codebase** the user named, dispatch the
`component-recommender` agent against that repo before drafting the table below (via a
sub-agent task where the host supports one, otherwise apply its method directly). Fold
its cited recommendations in as a starting draft. Skip this entirely for a greenfield
plugin with nothing to scan.

Then propose a component table, including the types you decided *not* to create:

```
| Component | Count | Purpose |
|-----------|-------|---------|
| Skills    | 3     | ...     |
| Agents    | 0     | Not needed |
| Commands  | 0     | Not needed (legacy layout) |
| Hooks     | 0     | Not needed |
| MCP       | 0     | Not needed |
| Settings  | 0     | Not needed |
```

**Default to skills** for everything the plugin does — both agent-invoked guidance and
user-invoked procedures (see `skill-development`). This marketplace is for Australian
advice and broking practices on Claude Code / Cowork. Only propose the legacy
`commands/` layout when extending a plugin that already uses it. Agents, hooks, MCP,
and settings are opt-in — most plugins need none. Catalogue plugins also need a
`practice-setup` skill and a `CLAUDE.md` practice-profile template. Start small: one
well-crafted skill beats five half-baked components.

**Get explicit confirmation of the table before writing anything.**

## Phase 3: Scaffold

Once the plan is confirmed, dispatch the `plugin-scaffolder` agent (or carry out the
same steps directly) with the confirmed name, component table, and repo root. It
creates the directory structure per `plugin-structure`, writes **this repo's**
manifest (`.claude-plugin/plugin.json` only — do not add `.cursor-plugin/` for a
practice plugin), a `CLAUDE.md` practice-profile template when the plugin is
catalogue-bound, and a non-empty `README.md`. Re-read what it wrote.

## Phase 4: Component authoring

For each confirmed row, load the matching skill before writing its files:

| Component | Skill to load first |
| :-------- | :------------------ |
| Skills | `skill-development` |
| Agents | `agent-development` |
| Commands (legacy) | `command-development` |
| Hooks | `hook-development` |
| MCP | `mcp-integration` |
| Settings (`.local.md`) | `plugin-settings` |

Apply the `plugin-portability` skill's rules to every component regardless of type.
After writing each skill, dispatch the `skill-reviewer` agent against it (or apply its
checklist) before moving on — a weak trigger description is cheaper to fix now than
after the plugin ships. If the plugin declares more than one swappable MCP server
across categories, follow `mcp-integration`'s `CONNECTORS.md` guidance; don't add one
for a single-server plugin.

## Phase 5: Validate

Dispatch the `plugin-validator` agent against the new plugin directory, and run this
repo's checks from `AGENTS.md` (`claude plugin validate`, `check-marketplace-sync.py`,
`validate-skills.py`, `validate-connectors.py`, `sync-references.py` as applicable).
There is no `scripts/validate.py` here. Fix every critical finding before continuing.

## Phase 6: Test locally

Load the plugin without installing it and exercise at least one skill with a prompt
that should trigger it — confirm it actually fires, not just that loading didn't error.
The mechanism is host-specific; use whichever this repo's contributor docs describe, or
ask the user how they normally test a plugin locally. If this repo has an automated
test suite, run it too.

## Phase 7: Register and release

This step registers a **practice** plugin in `.claude-plugin/marketplace.json` and,
if the user proceeds, commits and pushes. **Require explicit user confirmation.**
Load `marketplace-and-release` for the catalogue entry, then hand off to the
`release` skill for gates, version bump, commit, and push.

**Never register `plugin-management` itself** unless the user explicitly overrides
that. Maintainer tooling stays out of the adviser/broker catalogue.

## Packaging a standalone `.plugin` (Cowork hand-off)

If the user wants a shareable plugin file rather than (or as well as) a marketplace
entry — common in Cowork — package the directory as a `.plugin` archive after
validation passes. Zip into a temporary location first, then copy into the outputs
directory (writing directly there may fail on permissions):

```bash
cd /path/to/plugin && zip -r /tmp/<name>.plugin . -x "*.DS_Store" && cp /tmp/<name>.plugin /path/to/outputs/<name>.plugin
```

Name the file after the plugin's own `name` field. In Cowork the file shows as a rich
preview the user can browse and accept.

## Verification

- **Phases 3–4** — re-read every file just written: no truncation, correct frontmatter.
- **Phase 5** — confirm the audit reports no critical findings; re-run after any fix.
- **Phase 6** — confirm the plugin loaded and the exercised skill actually triggered.
- **Phase 7** — after registration, confirm the new catalogue entries resolve; after
  release, confirm the commit landed and every manifest flavor still matches.

## Summary

Report a concise result: the plugin name, components created, validation status, test
status, and whether it was registered/released or handed off as a `.plugin`. If
registration was deferred, remind the user the plugin works locally but isn't
installable by others until registered — point back at `marketplace-and-release`.

## Related skills and agents

- **`plugin-structure`** — the directory and manifest shape Phase 3 creates.
- **`skill-development`** / **`agent-development`** / **`command-development`** /
  **`hook-development`** / **`mcp-integration`** / **`plugin-settings`** — Phase 4
  component authoring, one per type.
- **`plugin-portability`** — the cross-cutting discipline applied throughout Phase 4.
- **`marketplace-and-release`** — Phase 7 catalogue registration.
- **`release`** — Phase 7 version bump, gates, commit, and push.
- **`customize-plugin`** — the counterpart for adapting an *existing* plugin rather
  than creating a new one.
- Agents: `component-recommender` (Phase 2), `plugin-scaffolder` (Phase 3),
  `skill-reviewer` (Phase 4), `plugin-validator` (Phase 5).
