---
name: marketing-review
description: >
  This skill should be used when the user asks to "check this marketing copy",
  "is this ad misleading", "DDO/TMD review this social post", "review this
  website banner", or wants a licensee-policy pass on adviser or broker
  promotional content before publish.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "advice-core practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Marketing Review

## When to use

Review copy (social, website, email campaign, seminar flyer) against misleading-conduct risk, DDO/TMD alignment when a TMD is supplied, and the licensee's marketing policy.

## What this skill does not do

- **Does not approve copy for publication** — flags gaps for the marketing/compliance owner.
- **Does not coach consumers through TMD gating questions.**
- **Does not rewrite into a sales pitch** that implies personal advice or guaranteed credit approval.

## Preconditions

| Input | If missing |
|---|---|
| The copy | Ask |
| Licensee marketing policy and/or TMD if product-specific | Proceed with general misleading-conduct + "no personal advice" checks; mark TMD as `INPUT NEEDED` |
| Channel and audience | Ask (retail public vs existing clients) |

## Provisional mode

No TMD and copy names a product: **do not** green-light; flag TMD missing as blocking for product-specific claims.

## Trust spine

- **Confidence bands** (`governance-tracking`): High = copy + TMD + licensee policy in session; Medium = copy + policy; Low = copy only — general flags, not a clearance.
- Per `../../references/trust-conventions.md` and, if installed, `financial-adviser` `ddo-tmd.md` (also at `../../references/ddo-tmd.md` when that plugin is present; otherwise apply the same rules: no invented TMD, no gating coaching).
- **Failure modes:** Incentive gaming — do not "pass" copy because it is close enough; no personal-advice implication; `[review]` on performance claims and ratings.
- **Escalation:** Past-performance, "best lender", "guaranteed approval", or advice-shaped "you should" → blocking.

## Workflow

1. Identify claims: returns, ratings, "best", approval, tax, "suitable for you".
2. Check: misleading/over-promise; personal-advice or credit-assistance implication; TMD consistency if TMD supplied; missing general-advice warning if the licensee uses one.
3. Severity: blocking / high / medium / low.
4. Do not rewrite into a new campaign unless asked — review first.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — not a publication clearance

CHANNEL / AUDIENCE: [...]
CLAIMS TABLE: claim | issue | severity | evidence needed
TMD: [sourced version | INPUT NEEDED | N/A]
PERSONAL ADVICE / CREDIT ASSISTANCE RISK: [...]
REVIEWER ACTION BEFORE PUBLISH: [...]
CONFIDENCE: [...]
```

## Worked example

**Input:** Facebook ad: "We'll get you the best home loan in Australia."

**Excerpt:** Blocking — superlative + implied outcome. Not a comparison the broker can evidence. Replace with process-factual copy; `[review]` licensee marketing policy.

## Quality checks before delivering

- [ ] Not framed as approval to publish
- [ ] TMD gating not performed
- [ ] Superlatives and guarantees flagged

## Propose profile update

When a stable marketing checklist or warning line surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/advice-core/CLAUDE.md` (licensee policy path → org profile), ask, write only on yes. Only `/advice-core:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Publication is a human/compliance action.
