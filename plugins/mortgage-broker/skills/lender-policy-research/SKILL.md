---
name: lender-policy-research
description: >
  This skill should be used when the user asks to "what's this lender's
  policy on", "LMI / LVR / PAYG policy", "summarise this credit policy PDF",
  or wants a policy note for the working file. Not a recommendation.
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
# Lender Policy Research

## When to use

Synthesise a **supplied** lender policy/credit guide (or panel extract) into a working note. Prefer the PDF in session over model memory — policy dates quickly.

## What this skill does not do

- **Does not decide this client meets policy.**
- **Does not replace the current lender guide.**

## Preconditions

| Input | If missing |
|---|---|
| Policy PDF or quoted extract, or explicit ask to flag model knowledge | If no document: `[model knowledge — verify]` only, not file-ready |
| Lender name and topic (LVR, LMI, self-employed, etc.) | Ask |

## Provisional mode

No primary doc: short unverified note, **not** for BID file.

## Trust spine

Per `../../references/trust-conventions.md`. Currency required — ask for the current guide.

- **Confidence bands** (`structured-aggregation`): High = dated policy in session; Low = training data.
- **Failure modes:** No client-fit decision; quote page/section.

## Workflow

1. Record lender, document title, date/version `[sourced]`.
2. Extract only the asked topic plus adjacent exceptions.
3. Flag ambiguity `[review]`.
4. Line: not a recommendation; verify against current guide before lodgement.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — policy note, not a recommendation

LENDER / DOCUMENT / DATE: [...]
TOPIC: [...]
EXTRACT: [...]
VERIFY BEFORE LODGEMENT
CONFIDENCE: [...]
```

## Worked example

**Input:** Lender guide dated last month, "max LVR 90% PAYG owner-occ with LMI above 80%".

**Excerpt:** Quoted with page `[sourced]`. Client-fit `[review]`.

## Quality checks before delivering

- [ ] Document date recorded or `[unverified]`
- [ ] No "this client is eligible"

## Propose profile update

When a stable policy-note template surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/mortgage-broker/CLAUDE.md`, ask, write only on yes. Only `/mortgage-broker:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
