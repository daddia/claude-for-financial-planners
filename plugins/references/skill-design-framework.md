# Skill design framework — claude-for-financial-planners

Adapted from the strategy marketplace framework. Mechanical checks: `scripts/validate-skills.py` and `scripts/sync-skill-permission-tiers.py`.

## Work shapes

Every skill declares exactly one `metadata.work_shape`:

| Value | What it is | Typical skills here |
|---|---|---|
| `hypothesis-driven-analysis` | Frames a testable claim and checks evidence | `file-review`, `ddo-tmd-check` |
| `option-evaluation` | Compares discrete choices; human picks | `serviceability-compare`, `breach-triage` |
| `structured-aggregation` | Collects and structures inputs without making the call | `practice-setup`, `fact-find`, `meeting-prep`, `crm-hygiene`, `apl-research`, `needs-analysis`, `lender-policy-research`, `application-assemble`, `complaint-intake`, `ai-governance-setup`, `audit-export` |
| `narrative-synthesis` | Turns material into a draft the human owns | `file-note`, `client-letter`, `soa-draft`, `roa-draft`, `bid-rationale` |
| `governance-tracking` | Status, deadlines, checklists over time | `marketing-review`, `annual-review-pack`, `trailbook-review` |

## Permission tiers

| Tier | `allowed-tools` | Skills |
|---|---|---|
| `advisory` | `Read, Grep, Glob` | Default |
| `artefact-writer` | `Read, Grep, Glob, Write` | `practice-setup`, `ai-governance-setup`, `audit-export` |

## Required headings

Every `SKILL.md`: `## Outputs`, `## Worked example`. Every skill except `practice-setup`: `## Propose profile update`.

## Output class

Default `draft-for-review`. Nothing in this marketplace is autonomous advice or credit assistance.
