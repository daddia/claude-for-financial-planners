---
name: marketplace-and-release
description: Explains how to register a finished plugin in its marketplace catalogue(s) and choose a `category` — then hand off version/commit/push to this repo's `release` skill if one exists, or a self-contained fallback if it doesn't. Use when the user asks to "register this plugin", "add it to the marketplace", or has just finished scaffolding a new plugin directory. For "release", "ship", or "cut a release", use the `release` skill instead.
---

# Marketplace and release

A plugin isn't installable from the catalogue until it's registered — building the
directory is necessary but not sufficient. This skill covers registration and
shipping.

**This repo:** single catalogue at `.claude-plugin/marketplace.json`. `source` is
`./plugins/<name>`. Category is `productivity`. Author matches first-party plugins
(Jonathan Daddia). Do **not** add `.cursor-plugin/marketplace.json`. Do **not**
register `plugin-management` unless the user explicitly asks. After a confirmed
register, hand off to the `release` skill (`skills/release/SKILL.md`) for gates,
version bump, commit, and push.

It does not assume any specific pre-existing release tooling: it looks for one and
uses it if found, and otherwise carries out the release itself using the generic
steps below.

Three worked examples live alongside this skill:

- [`examples/single-catalogue-registration.md`](examples/single-catalogue-registration.md)
- [`examples/dual-catalogue-registration.md`](examples/dual-catalogue-registration.md)
- [`examples/release-fallback-flow.md`](examples/release-fallback-flow.md) — the
  generic version/validate/commit/push flow end to end, for when no existing release
  automation is found.

## Step 1: Detect the marketplace catalogue shape

Before registering anything, look at how the repo already lists its plugins:

- **Dual catalogue** — separate `.claude-plugin/marketplace.json` and
  `.cursor-plugin/marketplace.json` files, each with a `plugins` array (this is the
  shape used by a repo that ships to both Claude Code and Cursor). If both exist,
  treat them as one logical catalogue that must stay identical — every registration
  below applies to both, in the same change.
- **Single catalogue** — one `marketplace.json` (or equivalent) at the repo root.
  Register once.
- **No catalogue file at all** — some hosts discover plugins by directory alone, with
  no separate registration step. If so, say so plainly and skip to Step 4; there's
  nothing to register.

Whichever shape you find, match it — don't introduce a second catalogue file the repo
didn't already have, and don't skip a catalogue the repo already maintains.

**Dual catalogue means both files ship together, every time — including outside git.**
If you're handing off a plugin as a standalone artifact (a zip, a tarball, a copy
pasted into a review tool) rather than pointing at the repo directly, that artifact
needs the same pairing the repo enforces: a plugin with a `.cursor-plugin/plugin.json`
but no corresponding `.cursor-plugin/marketplace.json` entry reachable from wherever
it's delivered is a Cursor install with nothing to discover it by. Before calling a
hand-off complete, confirm the artifact actually contains both catalogue files, not
just both plugin manifests.

## Step 2: Register the plugin entry

Add one entry per catalogue file, identical across all of them if there's more than
one:

```json
{
  "name": "my-plugin",
  "description": "One sentence a marketplace browser can act on — what it does, not just its name.",
  "source": "./plugins/my-plugin",
  "category": "productivity",
  "author": {
    "name": "Jonathan Daddia",
    "url": "https://github.com/daddia"
  }
}
```

Required fields here: `name`, `description`, `source`, `category`, `author` —
`source` must resolve to a directory containing `.claude-plugin/plugin.json`,
relative to the repo root (`./plugins/<name>`). `name`/`description`/`author` must
match the plugin manifest (`scripts/check-marketplace-sync.py`).

**Choosing `category`:** match whichever existing entry in the same catalogue is
closest to this plugin in ownership shape — cross-cutting developer tooling next to
other cross-cutting developer tooling, product-specific knowledge next to other
product-specific knowledge. Don't invent a new category string for a single plugin;
if every existing entry uses a different casing or naming convention than you'd
naturally pick, follow the existing convention rather than fixing it unilaterally
mid-registration.

## Step 3: Add a code-ownership entry, if this repo has one

If the repo has a `CODEOWNERS` file (or equivalent), add a line for the new plugin's
directory naming the owning team, following whatever pattern the existing entries use
— one comment line naming the owner, one path rule. Skip this step if the repo has no
such file; don't introduce the convention as a side effect of registering one plugin.

## Step 4: Validate before shipping

If this repo ships a structural validator (look for something like
`scripts/validate.py`, a `validate` script in `package.json`, or similar — the
`plugin-validator` agent in this plugin will find and run it for you if asked),
run it now and fix anything it flags. **This repo** has no `scripts/validate.py`;
run the checks listed in `AGENTS.md` instead. If no validator exists, at minimum
re-check by hand: the new catalogue entries resolve to real directories, the plugin's
manifest(s) have every required field, and every `SKILL.md` has frontmatter.

On a Claude Code host, also run the first-party CLI check regardless of whether this
repo has its own validator — it catches a different class of mistake (an unrecognized
or misspelled manifest field) that a repo-specific script may not check for:

```bash
claude plugin validate ./plugins/my-plugin --strict
```

`--strict` promotes unrecognized-field warnings to errors, which matters in CI: without
it, a typo'd field name (or one left over from copy-pasting another tool's manifest)
passes validation and loads anyway, silently doing nothing.

## Step 5: Version, commit, and push

**First, look for existing release automation in this repo** — this marketplace
ships a `release` skill at `plugins/plugin-management/skills/release/SKILL.md`
(also invoked as `/release` once this toolkit is installed). Also check for a
`release` script in `package.json`, a `Makefile` target named `release`, or
similar. If one exists, hand off to it rather than duplicating its logic; it likely
already encodes this repo's own versioning/commit/tag conventions.

**If no release automation exists**, carry out the release yourself:

1. **Determine the version bump.** If the plugin versions independently (each plugin
   has its own manifest version, as in a dual-catalogue marketplace), bump only the
   changed plugin's version. If the repo has one repo-wide version instead, bump that.
   Default to these semver rules unless the repo's own history suggests otherwise:

   | Bump | When |
   | :--- | :--- |
   | `patch` | Bug fixes, fixture/test updates, docs |
   | `minor` | New skills/agents/commands, new features — a **brand-new plugin's
     first release** is `0.1.0` regardless of this rule, since it isn't a bump to an
     existing version |
   | `major` | Breaking changes to a plugin's structure or public interface |

2. **Update the version field(s)**, keeping every manifest flavor for the same plugin
   in sync if there's more than one.
3. **Re-run the validator** (Step 4) to confirm the bump didn't introduce drift.
4. **Commit and push.** Match the repo's existing commit-message convention — check
   `git log` for recent messages before choosing a style (Conventional Commits
   `type(scope): summary` is common but not universal). Stage only the files this
   change touched.

⚠ Pushing to a shared branch is not fully reversible once others have pulled it.
**Require explicit user confirmation** before running the push, whichever path (existing
automation or the fallback above) produced it.

## Getting the update to users

Different hosts pick up a version bump differently — some auto-refresh installed
plugins on any bump, others need the user to explicitly update/reinstall, and a
brand-new plugin (as opposed to a bump to an existing one) sometimes needs a one-time
manual step (an admin re-importing the catalogue, for example) before it's visible to
everyone. If you don't know this repo's specific behaviour, say so explicitly rather
than assuming either "it just works" or "manual steps are always needed."

## Checklist

- [ ] Entry added only to catalogue files this repo already maintains (here: just
      `.claude-plugin/marketplace.json`) — do not invent `.cursor-plugin/marketplace.json`
- [ ] Did **not** register `plugin-management` unless the user explicitly asked
- [ ] `category` is `productivity` (or matches an existing closer entry)
- [ ] `name`/`description`/`author` match the plugin's `plugin.json`
- [ ] Code-ownership entry added, if this repo has that file
- [ ] `AGENTS.md` validators pass
- [ ] `claude plugin validate` passes on the plugin and the marketplace
- [ ] `release` skill used for version/commit/push; fallback flow only if that
      skill is unavailable, with explicit confirmation before the push

## Related skills

- **`plugin-structure`** — the manifest(s) this skill registers.
- **`release`** — gates, version bump, commit, and push after registration.
- **`plugin-portability`** — nothing to add for registration itself; the manifest layer is
  already the multi-host solution this skill plugs into.
