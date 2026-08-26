---
name: ddo-tmd-check
description: >
  This skill should be used when the user asks to "TMD check this", "DDO
  review", "is this copy consistent with the target market", or wants a
  distributor-side consistency check against a supplied Target Market
  Determination. Does not decide that a client is in the target market.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "financial-adviser practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# DDO / TMD Check

## When to use

Distributor-side check: is this research note, SOA product section, or marketing claim **consistent with a TMD the user supplied**? Complements `/advice-core:marketing-review`.

## What this skill does not do

- **Does not determine that a client is in or out of the target market** — `[review]` for the adviser/distributor.
- **Does not coach TMD gating questions** with a client.
- **Does not invent TMD content.**

## Preconditions

| Input | If missing |
|---|---|
| TMD document | Halt TMD-alignment; `INPUT NEEDED` |
| The copy or product section to check | Ask |

## Provisional mode

No TMD: do not run a fake check.

## Trust spine

Per `../../references/ddo-tmd.md` and `trust-conventions.md`.

- **Confidence bands** (`hypothesis-driven-analysis`): High = TMD + copy both in session, claims mapped; Low = missing TMD — stop.
- **Failure modes:** Analytical rigor — quote TMD clauses; adviser stays decision-maker on client fit.

## Workflow

1. Record TMD product, version, date `[sourced]`.
2. Extract claims from the user's copy.
3. Map each claim: consistent / tension / not addressed.
4. Client-fit: always `[review]` — not performed.
5. Reviewer action list.

## Output format

Follow `../../references/ddo-tmd.md` check shape. Stamp disclaimer. Not a clearance.

## Worked example

**Input:** TMD excludes consumers seeking capital preservation within 12 months; seminar slide says "safe park for cash you need next year".

**Excerpt:** Tension — slide conflicts with TMD exclusion. Blocking for that claim. Client-fit not assessed.

## Quality checks before delivering

- [ ] TMD version recorded
- [ ] No gating coaching
- [ ] No in/out-of-market decision on a named client

## Propose profile update

When a stable TMD-check checklist surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/financial-adviser/CLAUDE.md`, ask, write only on yes. Only `/financial-adviser:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
