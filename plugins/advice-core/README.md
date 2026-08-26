# advice-core

Shared practice setup, meeting prep, file notes, CRM hygiene, client communications, and marketing-content compliance review for Australian advice and broking practices. Ships the connector set and the licensed-human-review guardrail spine the other plugins reuse.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Practice Setup** | Licensee org profile + advice-core conventions | `/advice-core:practice-setup` |
| **Meeting Prep** | Prior file + CRM extract → internal briefing | `/advice-core:meeting-prep` |
| **File Note Writer** | Consented transcript → structured file note | `/advice-core:file-note` |
| **CRM Hygiene** | Notes → proposed field updates (not applied) | `/advice-core:crm-hygiene` |
| **Client Letter** | Appointment / doc-request / process emails | `/advice-core:client-letter` |
| **Marketing Review** | Copy vs misleading-conduct / TMD / licensee policy | `/advice-core:marketing-review` |

This plugin has no scheduled agents under `agents/`.

## What this plugin does NOT do

- **Personal advice or credit assistance** — it records, structures, and drafts operational comms.
- **Write to XPLAN or aggregator CRMs** — V1 has no first-party `~~crm` MCP; you confirm and paste.
- **Publish marketing** — review flags only; compliance/marketing owner publishes.
- **Send email** unless you confirm after the licensed-human gate.

## Getting started

Run `/advice-core:practice-setup` first. It writes `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md` (shared) and `.../advice-core/CLAUDE.md`.

Install **user-scoped**. Pair with [`financial-adviser`](../financial-adviser), [`mortgage-broker`](../mortgage-broker), and/or [`compliance`](../compliance).

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/advice-core:practice-setup` | practice-setup | Licensee + file-note/letter conventions |
| `/advice-core:meeting-prep` | meeting-prep | Internal pre-meeting pack |
| `/advice-core:file-note` | file-note | Consented transcript → file note |
| `/advice-core:crm-hygiene` | crm-hygiene | Proposed CRM field updates |
| `/advice-core:client-letter` | client-letter | Client-facing operational drafts |
| `/advice-core:marketing-review` | marketing-review | Promotional copy gap list |

## Trust spine

Canonical: [`references/trust-conventions.md`](./references/trust-conventions.md). Every output is a draft for a licensed human.

## Customization

See [CONNECTORS.md](./CONNECTORS.md). V1 skills work without connectors.
