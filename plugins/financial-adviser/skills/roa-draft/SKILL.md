---
name: roa-draft
description: >
  This skill should be used when the user asks to "draft an ROA", "Record of
  Advice", "further advice note", or "update the advice file without a new SOA".
  The adviser decides whether further advice is available; this skill scaffolds
  the ROA and flags when a new SOA may be required.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "financial-adviser practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# ROA Draft

## When to use

Further advice where the client already has an SOA and the **adviser** determines circumstances have not changed in a way that requires a new SOA. Shorter draft: what changed, what is recommended (adviser-authored), why, costs.

## What this skill does not do

- **Does not decide that an ROA is legally sufficient** — if circumstances look material, flag `[review]` for a new SOA (`/financial-adviser:soa-draft`).
- **Does not select products** or certify BID.

## Preconditions

| Input | If missing |
|---|---|
| Prior SOA date/scope (or extract) | Ask; do not assume an SOA exists |
| What changed (or "nothing material" as adviser states) | Ask |
| Adviser recommendation wording | Leave blank `[review]` |

## Provisional mode

Unclear whether circumstances changed: **do not** produce a clean ROA; produce a fork — ROA scaffold vs "consider new SOA" with `[review]`.

## Trust spine

Per `../../references/trust-conventions.md` and `soa-content.md` ROA section. Licensed-human gate before file-ready.

- **Confidence bands** (`narrative-synthesis`): High = prior SOA in session + adviser wording + sourced costs; Low = no prior SOA — halt.
- **Failure modes:** Adviser decides ROA vs SOA; no invented "no change" finding.

## Workflow

1. Confirm prior SOA exists in session.
2. List claimed changes vs prior circumstances — sourced.
3. If material change is apparent, flag new SOA `[review]` and still offer a thin ROA only if the adviser insists it is further advice.
4. Scaffold ROA; recommendation blank unless adviser-supplied.
5. Gate + audit log.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — ROA / further advice
PRIOR SOA: [date/scope sourced]
CHANGE ASSESSMENT: [adviser call — flagged if model sees material change]
RECOMMENDATION: [adviser-authored or BLANK]
COSTS: [sourced or INPUT NEEDED]
CONFIDENCE: [...]
```

## Worked example

**Input:** SOA 11 months ago; client wants to increase insurance inside super only; adviser states circumstances otherwise unchanged.

**Excerpt:** ROA scaffold on insurance increase only. `[review]` confirm no other circumstance change. Premium `INPUT NEEDED`.

## Quality checks before delivering

- [ ] Prior SOA referenced
- [ ] Material-change fork visible
- [ ] No model product pick

## Propose profile update

When a stable ROA-vs-SOA rule surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/financial-adviser/CLAUDE.md`, ask, write only on yes. Only `/financial-adviser:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
