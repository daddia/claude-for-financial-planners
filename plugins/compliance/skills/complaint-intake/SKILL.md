---
name: complaint-intake
description: >
  This skill should be used when the user asks to "draft a complaint
  acknowledgement", "log this complaint", "IDF letter", "assemble the
  complaint file", or needs a structured intake for an AFCA-trackable
  complaint. Does not decide the outcome.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "compliance practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Complaint Intake

## When to use

Structure a complaint: acknowledgement draft, file-assembly list, SLA vs profile. Human owns IDF and AFCA.

## What this skill does not do

- **Does not decide the complaint** or admit liability.
- **Does not lodge with AFCA.**
- **Does not send** the acknowledgement unless gated and destination-checked.

## Preconditions

| Input | If missing |
|---|---|
| What the complainant said (paste/email) | Ask |
| SLA / template from profile | Use placeholders; flag INPUT NEEDED dates |

## Provisional mode

Incomplete identity: acknowledge what you can; `INPUT NEEDED` for the rest — do not guess client codes.

## Trust spine

Per `../../references/trust-conventions.md`. Sensitive content; destination check before `~~email` / `~~chat`.

- **Confidence bands** (`structured-aggregation`): High = complaint text + template; Low = one-line "client unhappy" — ask more.
- **Failure modes:** No liability language; no silent "we'll refund".

## Workflow

1. Capture: date received, channel, allegations in the complainant's words (quoted), products/loans referenced, outcome sought if stated.
2. Acknowledgement draft: receipt, SLA, contact, **no merits**.
3. File-assembly checklist.
4. Flag if `/compliance:breach-triage` may also be needed (potential reportable situation) without deciding it.
5. Gate before send.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — intake, not an outcome

ALLEGATIONS (quoted): [...]
ACKNOWLEDGEMENT DRAFT: [...]
FILE TO ASSEMBLE: [...]
SLA: [sourced from profile or INPUT NEEDED]
DO NOT ADMIT LIABILITY
CONFIDENCE: [...]
```

## Worked example

**Input:** Email "you put me in the wrong fund and I lost money."

**Excerpt:** Quote allegation. Ack draft without conceding unsuitable advice. Point at file-review + possible breach-triage `[review]`.

## Quality checks before delivering

- [ ] No merits decision
- [ ] No invented SLA
- [ ] Not sent unless gated

## Propose profile update

When a stable ack template or SLA surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/compliance/CLAUDE.md`, ask, write only on yes. Only `/compliance:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
