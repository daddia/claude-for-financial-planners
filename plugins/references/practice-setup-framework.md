# Practice setup framework — claude-for-financial-planners

Every first-party plugin's `practice-setup` skill follows this framework. Plugin skills add only **plugin-specific** questions on top; licensee-wide facts live once in the shared org profile.

## Invocation

| Command | Behaviour |
|---|---|
| `/<plugin>:practice-setup` | Detect existing setup; offer quick vs full if mode not specified |
| `/<plugin>:practice-setup --quick` | Short path: org gaps (if any) + 3–5 plugin questions; sensible defaults elsewhere |
| `/<plugin>:practice-setup --full` | Full org interview (when needed) + full plugin interview; review seed documents |
| `/<plugin>:practice-setup --redo` | Ignore existing profiles for this run; re-interview and overwrite on confirmation |
| `/<plugin>:practice-setup --check-integrations` | Report MCP connector status for this plugin; no interview unless user asks to continue |
| `/<plugin>:practice-setup --resume` | Continue a paused interview from the saved session file |

Combine flags when useful (e.g. `--redo --full`). If `--resume` is present, load the session first; other flags adjust what happens after resume.

## Config paths

| File | Purpose |
|---|---|
| `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md` | Shared licensee facts — written once, read by every plugin |
| `~/.claude/plugins/config/claude-for-financial-planners/<plugin>/CLAUDE.md` | Plugin practice profile — plugin-specific conventions only |
| `~/.claude/plugins/config/claude-for-financial-planners/<plugin>/practice-setup-resume.json` | Paused interview state |

**In-repo templates (read-only):** `../../references/org-profile-template.md` and the plugin's `../../CLAUDE.md`. Never modify installed plugin templates.

**Install scope:** User-scoped install (recommended) lets skills read files you reference anywhere on disk. Project-scoped install limits reads to the project folder — note this if the user reports "can't read [file]" during seed-document review.

## Startup — detect existing setup

Before asking questions:

1. **Read** `org-profile.md` if it exists. Note `Status` (`template` vs `complete`) and which sections are filled.
2. **Read** `~/.claude/plugins/config/claude-for-financial-planners/<plugin>/CLAUDE.md` unless `--redo` is set.
3. **If both exist and are complete** (not `template`, no major blanks): summarize what's on file and ask — refresh org profile, refresh plugin profile, both, or `--check-integrations` only? Do not re-interview unless the user chooses refresh or passed `--redo`.
4. **If only org profile exists:** say the org layer is done; run plugin-specific interview only.
5. **If only plugin profile exists** (legacy): offer to backfill org profile from plugin content where possible, then continue.
6. **If neither exists:** explain the two-layer model (licensee once, plugin per practice area) and proceed.

### Legacy migration

If an old practice profile at a non-standard path is found, offer to copy normalized content into the standard paths above. Do not delete the legacy file without explicit confirmation.

## Org profile interview

Run when `org-profile.md` is missing, `Status` is `template`, `--redo` is set, or `--full` requires org refresh. **Skip sections already answered** in a complete org profile unless `--redo`.

Ask (quick: licensee identity + licence type/number + practice type + CRM + house tone + data-handling posture; full: all):

1. **Licensee identity** — legal name, trading name, how you refer to it in prose.
2. **Licence** — AFSL, ACL, or both; licence number(s); authorised-representative vs licensee staff; responsible manager name if they want it on file.
3. **Practice type** — advice, broking, dual; typical client (retail, wholesale, SMSF, first-home, refinance, etc.).
4. **Compliance owner** — who signs off advice/credit files; escalation path for complaints and potential reportable situations.
5. **Approved Product List / lender panel** — where it lives; who maintains it; how current.
6. **Templates and clause library** — SOA/ROA/CAR, file-note, BID rationale, FSG/credit guide locations.
7. **Systems of record** — CRM / practice management (`~~crm`), document store (`~~documents`), lodgement (ApplyOnline or equivalent), e-sign (`~~e-signature`).
8. **Data handling** — Australian hosting preference, APP posture, what must never leave the licensee environment, December 2026 ADM disclosure owner.
9. **House writing style** — tone with clients, things to avoid, branding.
10. **AI-use governance** — whether an AI inventory and human-accountability map already exist (full interview points at `/compliance:ai-governance-setup`).
11. **PI / AFCA** — note that PI is the licensee's obligation; AFCA is EDR. Do not collect policy numbers unless the user volunteers them.

**Write org profile** to `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md` following `org-profile-template.md`. Set `Status: complete` when done. User confirmation on the org summary authorizes the write.

## Plugin profile interview

After org layer is satisfied:

1. **Read org profile** and **do not re-ask** facts already captured there.
2. Run the **plugin-specific** questions defined in the skill.
3. **Quick mode:** plugin-specific essentials only; seed documents optional.
4. **Full mode:** request 2–3 seed documents listed in the plugin skill; read for tone, structure, and vocabulary — not to copy proprietary content or client PII into the profile. Redact names if the user pastes live files.
5. **Write plugin profile** to `~/.claude/plugins/config/claude-for-financial-planners/<plugin>/CLAUDE.md`. Fill every section; use "no strong preference — will infer per task" or "see org profile" rather than leaving blanks.

## Integrations — `--check-integrations`

Read the installed plugin's `.mcp.json` (in-repo: `../../.mcp.json` from the skill). For each server, report:

| Server | Enables in this marketplace |
|---|---|
| slack | Watcher alerts, team notifications |
| gmail | Email context, client comms drafts |
| google-drive | Seed documents, templates, file notes |
| google-calendar | Meeting prep, FDS/review deadline watchers |
| notion | Clause library / knowledge base |
| microsoft-graph-enterprise | Outlook, SharePoint, Teams when Agent365 MCP is enabled |

For each: **connected** (user has authorized), **available but not connected**, or **not in this plugin's manifest**. Name which agents/skills are degraded without each connector. Note that `~~crm` (XPLAN, aggregator CRMs, ApplyOnline) has **no first-party MCP** in V1 — user uploads remain the fallback. Offer to continue setup after the report.

## Pause and resume

**Pause:** If the user must stop mid-interview, write `practice-setup-resume.json` with: `plugin`, `mode` (quick/full), `started_at`, `org_complete` (bool), `answers` (object of field → value), `remaining_steps` (array), `last_step_completed`. Tell the user to run `/<plugin>:practice-setup --resume`.

**Resume:** Load the session file, summarize progress, continue from `remaining_steps`. Delete the session file after successful write of both profiles (or on `--redo` completion).

## Confirm and summarize

1. Show **org profile** changes (if any) and **plugin profile** changes in plain language.
2. Wait for explicit confirmation before writing.
3. After write: remind user they can edit files directly, use **propose profile update** from other skills, run `--check-integrations`, or `--redo` for a full refresh.
4. Mention `org-profile.md` is shared — other plugins will reuse it on their first practice-setup.
5. Restate the standing rule: every subsequent skill output is a **draft for licensed human review**.

## Living profile rules

- **`practice-setup`** is the only skill that may **auto-apply** a full profile write (after confirmation above).
- **Every other skill** uses **propose profile update** for stable conventions — show exact diff, ask, write only on yes.
- Org-level stable facts discovered later → propose update to `org-profile.md`. Plugin-specific facts → propose update to the plugin `CLAUDE.md`.
