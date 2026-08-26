---
name: bid-rationale
description: >
  This skill should be used when the user asks to "draft the BID file note",
  "why this loan", "best interests rationale", "credit assistance file note",
  or needs a Part 3-5A / RG 273 structured rationale. The broker authors the
  recommendation; this skill scaffolds evidence.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "mortgage-broker practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# BID Rationale

## When to use

Draft the consumer-credit Best Interests Duty file note / "why this loan" after the **broker** has chosen among options. Scaffold from needs analysis + comparison working.

## What this skill does not do

- **Does not certify that BID is met** (no safe harbour under RG 273).
- **Does not pick the loan.**
- **Does not apply to commercial credit.**

## Preconditions

| Input | If missing |
|---|---|
| Needs analysis + comparison with ≥2 options | Ask; refuse to rationalise a single undocumented option |
| Broker's chosen option and their reasons (even bullet points) | Leave recommendation blank; do not infer from the cheapest rate |

## Provisional mode

Broker has not chosen: do not write a "why this loan"; send them to `serviceability-compare`.

## Trust spine

Per `../../references/nccp-broker-bid.md` and `trust-conventions.md`. Cost/affordability visible. Conflicts/remuneration recorded from user input only.

- **Confidence bands** (`narrative-synthesis`): High = comparison sourced + broker wording; Low = missing options — halt.
- **Failure modes:** Broker is decision-maker; no one-size template that ignores this client's cost facts.

## Workflow

1. Confirm NCCP consumer credit.
2. Structure: requirements; financial situation (as provided); options considered; cost comparison; net benefit factors; discarded options; conflicts; **recommendation in broker's words**.
3. Tag every rate/fee.
4. Licensed-human gate before file-ready. Audit log.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — BID rationale scaffold, not a BID certificate

REQUIREMENTS / SITUATION: [...]
OPTIONS CONSIDERED: [...]
COST / AFFORDABILITY: [...]
NET BENEFIT WORKING: [...]
CONFLICTS / REMUNERATION: [sourced or INPUT NEEDED]
RECOMMENDATION: [broker-authored]
AUDIT LOG: [...]
CONFIDENCE: [...]
```

## Worked example

**Input:** Three-lender table; broker writes "choosing B for offset + lower cash-out fees despite 5bp higher rate".

**Excerpt:** Quotes broker reason `[sourced: user]`. Rate/fee table from comparison. Does not add extra reasons the broker did not give.

## Quality checks before delivering

- [ ] Multiple options on file
- [ ] Recommendation not model-authored
- [ ] Not labelled as BID certified

## Propose profile update

When a stable BID template surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/mortgage-broker/CLAUDE.md`, ask, write only on yes. Only `/mortgage-broker:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Signing is a human action.
