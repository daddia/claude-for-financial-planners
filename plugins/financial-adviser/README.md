# financial-adviser

AFSL-scoped drafting support for Australian financial advisers — fact-find structure, SOA/ROA/Client Advice Record drafts, annual review packs, APL research, and DDO/TMD checks. **The adviser sets the strategy, owns the recommendation, and remains the authorising signatory.**

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Practice Setup** | SOA/CAR regime, APL, FDS cadence | `/financial-adviser:practice-setup` |
| **Fact-Find** | Discovery notes → gap-led fact-find | `/financial-adviser:fact-find` |
| **SOA Scaffolder** | Fact-find + adviser-authored strategy → SOA or CAR draft | `/financial-adviser:soa-draft` |
| **ROA Scaffolder** | Further advice draft; flags when a new SOA may be needed | `/financial-adviser:roa-draft` |
| **Review Pack** | Annual review / FDS / consent pack scaffold | `/financial-adviser:annual-review-pack` |
| **APL Research** | General product note against the APL | `/financial-adviser:apl-research` |
| **TMD Check** | Copy/product section vs supplied TMD | `/financial-adviser:ddo-tmd-check` |
| **FDS / Renewal Watcher** | Deadline reminder | scheduled agent |

## What this plugin does NOT do

- **Provide personal advice** or select APL products for a client.
- **Certify BID** (s961B/s961G/s961J) or treat safe-harbour steps as passed — or as repealed.
- **Default to Client Advice Record** — SOA unless the licensee confirms CAR applies (DBFO staged).
- **Act as a digital advice provider** under RG 255.

## Getting started

Install [`advice-core`](../advice-core) first (shared org profile and trust spine), then `/financial-adviser:practice-setup`.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/financial-adviser:practice-setup` | practice-setup | Advice-document regime, APL, review cadence |
| `/financial-adviser:fact-find` | fact-find | Gap-led fact-find |
| `/financial-adviser:soa-draft` | soa-draft | SOA (default) or CAR scaffold |
| `/financial-adviser:roa-draft` | roa-draft | Further advice scaffold |
| `/financial-adviser:annual-review-pack` | annual-review-pack | Review / FDS pack |
| `/financial-adviser:apl-research` | apl-research | General APL research note |
| `/financial-adviser:ddo-tmd-check` | ddo-tmd-check | TMD consistency check |
| scheduled | fds-renewal-watcher | Review/FDS reminders |

## References

- [`bid-s961b.md`](./references/bid-s961b.md) — BID scaffolding (verify current law)
- [`soa-content.md`](./references/soa-content.md) — SOA/ROA/CAR headings
- [`ddo-tmd.md`](./references/ddo-tmd.md)
- Shared trust spine copy: [`trust-conventions.md`](./references/trust-conventions.md)

## Customization

[CONNECTORS.md](./CONNECTORS.md). No first-party XPLAN MCP in V1.
