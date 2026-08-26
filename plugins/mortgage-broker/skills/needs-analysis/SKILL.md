---
name: needs-analysis
description: >
  This skill should be used when the user asks to "structure a loan needs
  analysis", "client interview for a home loan", "what's missing from this
  credit fact find", or needs a gap-led needs analysis before serviceability
  or BID work.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "mortgage-broker practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Needs Analysis

## When to use

Structure consumer-credit discovery: objectives, security, occupancy, income/expenses, existing debts, timeline. Gap list — not a lender pick.

## What this skill does not do

- **Does not provide credit assistance** or pick a lender.
- **Does not run serviceability** — that is `serviceability-compare` using the broker's calculator outputs.
- **Does not apply BID to commercial lending** — halt BID path if commercial.

## Preconditions

| Input | If missing |
|---|---|
| Interview notes or intake | Ask |
| NCCP vs commercial | Ask; if commercial, label out of Part 3-5A |

## Provisional mode

Thin notes: headings + `INPUT NEEDED`.

## Trust spine

Per `../../references/trust-conventions.md` and `nccp-broker-bid.md`. Do not invent income or LVR.

- **Confidence bands** (`structured-aggregation`): High = sourced intake; Low = headings only.
- **Failure modes:** Support not assistance; RG 209 verification remains the licensee's process — flag, don't certify.

## Workflow

1. Confirm consumer credit vs commercial.
2. Map: objectives, property/occupancy, amount/LVR if stated, income/expenses, existing credit, buffers, timeline, special features (offset, redraw, fixed/variable preferences as **client-stated**, not recommended).
3. Incomplete-information list.
4. Next step pointers — no winner.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — needs analysis, not a recommendation

REGIME: NCCP consumer | commercial (BID skills stop)
SECTIONS: [sourced | INPUT NEEDED]
INCOMPLETE INFORMATION: [...]
NOT A LENDER RECOMMENDATION
CONFIDENCE: [...]
```

## Worked example

**Input:** First-home notes; income stated; expenses blank; no savings evidence.

**Excerpt:** Expenses and genuine savings INPUT NEEDED. Do not imply serviceability.

## Quality checks before delivering

- [ ] No lender named as "best"
- [ ] Commercial boundary explicit
- [ ] Blanks stay blank

## Propose profile update

When a stable needs-analysis heading set surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/mortgage-broker/CLAUDE.md`, ask, write only on yes. Only `/mortgage-broker:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `lender-policy-research` / `serviceability-compare`.
