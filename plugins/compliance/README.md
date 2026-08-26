# compliance

Licensee compliance support for Australian advice and credit practices — file-review checklists, complaint intake, reportable-situation triage, REP 798 AI-use governance setup, and 7-year audit-export drafts. **Assists the reviewer; does not certify.**

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Practice Setup** | Checklists, complaint SLA, aging, export path | `/compliance:practice-setup` |
| **File Reviewer** | Draft file → gap list | `/compliance:file-review` |
| **Complaint Intake** | Acknowledgement + file assembly (no merits) | `/compliance:complaint-intake` |
| **Breach Triage** | Options for the human on a possible incident | `/compliance:breach-triage` |
| **AI Governance** | REP 798 inventory + policy skeleton | `/compliance:ai-governance-setup` |
| **Audit Export** | Reconstructable pack of inputs/drafts | `/compliance:audit-export` |
| **File-Aging Watcher** | Files past review threshold | scheduled agent |
| **Regulatory Change Watcher** | ASIC/Treasury/APRA bulletin draft | scheduled agent |

## What this plugin does NOT do

- **Certify** BID, responsible lending, TMD fit, or file completeness.
- **Decide** that a situation is or is not reportable to ASIC.
- **Lodge** with AFCA or ASIC.
- **Replace** the licensee's compliance function or legal counsel.

## Getting started

Install [`advice-core`](../advice-core) first (org profile), then `/compliance:practice-setup`. If the practice has no AI inventory, run `/compliance:ai-governance-setup` next.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/compliance:practice-setup` | practice-setup | Review/complaint/audit conventions |
| `/compliance:file-review` | file-review | Gap list, not a clearance |
| `/compliance:complaint-intake` | complaint-intake | Ack draft + file list |
| `/compliance:breach-triage` | breach-triage | Options, not a legal finding |
| `/compliance:ai-governance-setup` | ai-governance-setup | REP 798 inventory |
| `/compliance:audit-export` | audit-export | Reconstructable pack |
| scheduled | file-aging-watcher | Aging reminders |
| scheduled | regulatory-change-watcher | Regulatory bulletin |

## References

- [`ai-governance-rep798.md`](./references/ai-governance-rep798.md)
- [`record-keeping.md`](./references/record-keeping.md)
- Shared trust spine: [`trust-conventions.md`](./references/trust-conventions.md)

## Customization

[CONNECTORS.md](./CONNECTORS.md). Watchers need `~~chat` (and `~~calendar` where dates live) or they write workspace files.
