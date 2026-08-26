---
name: annual-review-pack
description: >
  This skill should be used when the user asks to "prepare the annual review",
  "renewal pack", "FDS draft", "ongoing fee consent", "review meeting pack",
  or to flag Fee Disclosure Statement / consent deadlines for an advice client.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "financial-adviser practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Annual Review Pack

## When to use

Assemble an annual/ongoing-service review pack: last advice, portfolio/holdings extract, FDS/consent drafts as **templates to complete**, deadline flags. Adviser runs the review meeting.

## What this skill does not do

- **Does not give a new recommendation** — that is `soa-draft` / `roa-draft` after the adviser decides.
- **Does not calculate FDS figures** unless sourced from licensee fee system extract.
- **Does not send** the pack to the client.

## Preconditions

| Input | If missing |
|---|---|
| Client / review date / last SOA date | Ask; `~~calendar` if connected |
| Holdings / fee extract | `INPUT NEEDED` — do not invent performance or fees |
| FDS / consent templates | Use labelled placeholders |

## Provisional mode

No fee extract: pack without FDS numbers; flag blocking for client send.

## Trust spine

Per `../../references/trust-conventions.md`. Performance figures `[sourced]` or omitted. DBFO fee-consent rules are **in-flight historically** — use the licensee's current templates, not model memory of the Act.

- **Confidence bands** (`governance-tracking`): High = dates + fee extract + prior SOA; Low = date only.
- **Failure modes:** Do not "pass" an overdue FDS; do not invent returns.

## Workflow

1. Read FDS/consent lead time from profile.
2. Deadline table: review meeting, FDS, consent, risk-profile age.
3. Pack contents list + drafted invitation (`/advice-core:client-letter` style — no advice).
4. Placeholder FDS/consent using licensee template structure.
5. Gate before client-facing pack.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — review pack, not new advice

DEADLINES: [item | date sourced | status]
PACK CONTENTS: [...]
FDS / CONSENT: [template with INPUT NEEDED figures]
REVIEW AGENDA (questions): [...]
CONFIDENCE: [...]
```

## Worked example

**Input:** Review in 10 days; FDS anniversary in 18 days; profile lead time 30 days.

**Excerpt:** FDS lead-time **breached** vs profile `[review]`. Do not invent FDS dollar table. Invitation draft only.

## Quality checks before delivering

- [ ] No new product advice
- [ ] No invented fees or returns
- [ ] Overdue items not smoothed over

## Propose profile update

When a stable FDS lead time or pack contents list surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/financial-adviser/CLAUDE.md`, ask, write only on yes. Only `/financial-adviser:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Watcher: `fds-renewal-watcher` when scheduled.
