# Quick Start

**60 seconds.** This gets you to your first slash command. Allow 10–20 minutes per plugin if you want a filled practice profile before serious client-file work.

## Install in Claude Cowork

1. Open the **Cowork** tab.
2. Click **Customize** in the left sidebar.
3. Click **Browse plugins** and install what you need, **or** upload a plugin directory as a zip.

## Install in Claude Code

1. **Open Claude Code** (terminal) or **Claude Cowork** (desktop app).

2. **Add the marketplace.** Type `/plugin marketplace add ` (with a space at the end), then **drag the unzipped `claude-for-financial-planners` folder onto the terminal** — it fills in the path. Press Enter.

   Or type the full path: `/plugin marketplace add /Users/you/Projects/claude-for-financial-planners`

3. **Install your plugin.** Start with `advice-core`, then add the profession plugin that matches your licence:

   ```
   /plugin install advice-core@claude-for-financial-planners
   /plugin install financial-adviser@claude-for-financial-planners
   /plugin install mortgage-broker@claude-for-financial-planners
   /plugin install compliance@claude-for-financial-planners
   ```

4. **Restart Claude Code.** Not optional — the plugin is not live until you restart.

5. **Run setup.** Takes 2 minutes (`--quick`) or 10–20 minutes (`--full`). The first plugin you set up also writes a shared licensee org profile reused by the others.

   ```
   /advice-core:practice-setup
   /advice-core:practice-setup --quick
   /advice-core:practice-setup --check-integrations
   ```

   Other flags: `--full`, `--redo`, `--resume`.

6. **Connect your tools (optional).** Skills work without connectors. In Cowork: Settings → Connectors. In Claude Code: each plugin lists MCP servers in `.mcp.json`. There is **no first-party XPLAN or ApplyOnline MCP in V1** — paste CRM extracts.

## Install user-scoped, not project-scoped

When `/plugin install` asks, **pick user scope** unless each client repo must carry its own profile with no leakage. Project scope blocks reads outside the project folder (Downloads, shared drives). User scope does not grant extra access — it only lets the plugin read files you explicitly reference, from any folder.

## Which plugin is for me?

| You are a… | Install… | First command |
|---|---|---|
| Adviser, paraplanner, or advice assistant | `advice-core` + `financial-adviser` | `/advice-core:practice-setup` then `/financial-adviser:practice-setup` |
| Mortgage broker or credit representative | `advice-core` + `mortgage-broker` | `/advice-core:practice-setup` then `/mortgage-broker:practice-setup` |
| Dual advice + broking practice | all four | advice-core first (writes org profile) |
| Compliance / responsible manager | `advice-core` + `compliance` | `/compliance:practice-setup` then `/compliance:ai-governance-setup` |

After setup, run the skill that matches the job — see each plugin README. Examples: `/advice-core:file-note`, `/financial-adviser:soa-draft`, `/mortgage-broker:bid-rationale`, `/compliance:file-review`.

## What you're installing

Each plugin learns your playbook through practice setup. Licensee-wide facts go to `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md` (written once, shared). Plugin-specific conventions go to `~/.claude/plugins/config/claude-for-financial-planners/<plugin>/CLAUDE.md`. Every skill reads both.

**Every output is a draft for licensed human review.** The plugins flag what they're unsure about, tag product facts and dollar amounts by source, surface incomplete information, and gate send/lodge/file. You review, edit, sign, and take responsibility. They are not personal advice, not credit assistance, and not a digital advice provider under RG 255.

## Stuck?

- **Plugin not visible after install** → `/plugin marketplace list` should show `claude-for-financial-planners`. Then restart (step 4).
- **Slash command not found** → you skipped restart.
- **Practice profile not loading** → run `/<plugin>:practice-setup`. Profiles live under `~/.claude/plugins/config/claude-for-financial-planners/`.
- **Can't read a file outside the project** → reinstall **user-scoped**.
- **CRM / XPLAN / ApplyOnline not connected** → expected in V1; paste extracts.
