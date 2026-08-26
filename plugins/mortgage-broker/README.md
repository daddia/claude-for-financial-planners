# mortgage-broker

ACL-scoped drafting support for Australian mortgage brokers — needs analysis, lender-policy research, serviceability comparison, application-assembly assist, Best Interests Duty rationale, and trail-book/repricing review. **The broker owns the recommendation and the BID file.** NCCP consumer credit only for BID skills.

## Agents

| Agent | What it does | Command |
|---|---|---|
| **Practice Setup** | Panel, aggregator, BID template, trail cadence | `/mortgage-broker:practice-setup` |
| **Needs Analysis** | Interview notes → gap-led needs analysis | `/mortgage-broker:needs-analysis` |
| **Policy Research** | Lender guide extract → working note | `/mortgage-broker:lender-policy-research` |
| **Comparison Working** | Calculator outputs → multi-lender table (no winner) | `/mortgage-broker:serviceability-compare` |
| **Application Assemble** | Doc checklist for lodgement (does not lodge) | `/mortgage-broker:application-assemble` |
| **BID File Note** | Broker-authored choice → rationale scaffold | `/mortgage-broker:bid-rationale` |
| **Trail Book Review** | Expiry extract → conversation watchlist | `/mortgage-broker:trailbook-review` |
| **Trail Book Watcher** | Cadence reminder | watcher agent (on demand) |

## What this plugin does NOT do

- **Credit assistance** until you decide, edit, and sign.
- **Calculate serviceability** or replace Quickli / lender calculators.
- **Pick a winner** or certify BID (RG 273 — **no safe harbour**).
- **Lodge to ApplyOnline** — no first-party lodgement MCP in V1.
- **Apply Part 3-5A BID to commercial lending.**

## Getting started

Install [`advice-core`](../advice-core) first, then `/mortgage-broker:practice-setup`.

## Skill & command reference

| Command | Skill | What it does |
|---|---|---|
| `/mortgage-broker:practice-setup` | practice-setup | Panel, BID, trail cadence |
| `/mortgage-broker:needs-analysis` | needs-analysis | Gap-led needs analysis |
| `/mortgage-broker:lender-policy-research` | lender-policy-research | Policy note from a supplied guide |
| `/mortgage-broker:serviceability-compare` | serviceability-compare | Multi-option working |
| `/mortgage-broker:application-assemble` | application-assemble | Lodgement checklist |
| `/mortgage-broker:bid-rationale` | bid-rationale | BID file-note scaffold |
| `/mortgage-broker:trailbook-review` | trailbook-review | Internal expiry watchlist |
| watcher (on demand) | trailbook-opportunity-watcher | Weekly reminder |

## References

- [`nccp-broker-bid.md`](./references/nccp-broker-bid.md)
- Shared trust spine: [`trust-conventions.md`](./references/trust-conventions.md)

## Customization

[CONNECTORS.md](./CONNECTORS.md).
