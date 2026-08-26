---
name: serviceability-compare
description: >
  This skill should be used when the user asks to "compare lenders",
  "serviceability comparison", "net benefit working", "which lenders might
  fit this scenario", or wants a comparison table from calculator outputs
  and policy notes. The broker interrogates and owns the recommendation.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "mortgage-broker practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Serviceability Compare

## When to use

Synthesise **broker-supplied** serviceability results (Quickli, lender calcs) and policy notes into a comparison / net-benefit **working**. More than one option. Broker decides.

## What this skill does not do

- **Does not calculate serviceability** or replace Quickli/lender calculators.
- **Does not pick a winner** or present a ranking as the client's loan.
- **Does not certify BID or responsible lending.**

## Preconditions

| Input | If missing |
|---|---|
| At least two options (lenders/products) the broker is considering | Ask; refuse a one-lender "comparison" for NCCP BID work |
| Serviceability outputs or explicit "not run yet" | Do not invent borrowing capacity |
| Scenario facts (from needs analysis) | Ask |

## Provisional mode

Policy from model knowledge only: every policy cell `[model knowledge — verify]`; **structured first pass**; not for the client file.

## Trust spine

Per `../../references/trust-conventions.md` and `nccp-broker-bid.md`. RG 273: cost/affordability; no one-size-fits-all; **no safe harbour**.

- **Confidence bands** (`option-evaluation`): High = calculator extracts + current policy PDFs; Medium = calculator only; Low = no numbers — structure only.
- **Failure modes:** Broker stays decision-maker; do not hide commissions; commercial lending out of BID.

## Workflow

1. Confirm NCCP consumer credit.
2. Table: lender/product | rate/fees `[sourced]` | assessed serviceability `[sourced from calc]` | policy notes `[sourced or verify]` | features client asked about | remuneration if provided.
3. Net-benefit **working** as factors, not a conclusion.
4. Discarded options: only if the broker stated why, or label `[review]`.
5. Recommendation line **blank** unless broker supplied wording.
6. Gate before any client-facing comparison.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — comparison working, not credit assistance

OPTIONS TABLE: [...]
NET BENEFIT FACTORS (not a winner): [...]
RECOMMENDATION: BLANK or [broker-authored]
INCOMPLETE INFORMATION: [...]
CONFIDENCE: [...]
```

## Worked example

**Input:** Three panel lenders; Quickli screenshot; client wants offset; broker has not chosen.

**Excerpt:** Table of three. Offset column sourced from policy PDFs. No rank order. Recommendation blank.

## Quality checks before delivering

- [ ] ≥2 options for NCCP
- [ ] No invented serviceability
- [ ] No implicit winner (watch sort order — use broker's input order or alphabetical, say which)

## Propose profile update

When a stable comparison-column set surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/mortgage-broker/CLAUDE.md`, ask, write only on yes. Only `/mortgage-broker:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `bid-rationale` after the broker chooses.
