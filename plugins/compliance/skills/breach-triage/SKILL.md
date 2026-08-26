---
name: breach-triage
description: >
  This skill should be used when the user asks to "is this reportable",
  "breach assessment", "reportable situation triage", "incident assessment
  for compliance", or needs options for a human deciding a possible AFSL/ACL
  incident. Does not decide.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "compliance practice"
  review_cadence: "quarterly"
  work_shape: "option-evaluation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Breach Triage

## When to use

Help the **accountable human** structure a possible reportable-situation / breach assessment: facts, options, what to check in the licensee's policy. The human decides.

## What this skill does not do

- **Does not determine that a situation is or is not reportable** to ASIC.
- **Does not notify ASIC or AFCA.**
- **Does not invent the legal test** — point at the licensee's policy and current law `[verify]`.

## Preconditions

| Input | If missing |
|---|---|
| Incident facts | Ask |
| Licensee breach/reportable-situation policy if available | Proceed with questions only; `INPUT NEEDED` policy |

## Provisional mode

Thin facts: questions, not a scored outcome.

## Trust spine

Per `../../references/trust-conventions.md`. Legislated thresholds and time limits `[verify]` unless the policy in session states them.

- **Confidence bands** (`option-evaluation`): High = facts + licensee policy in session; Low = facts only — options labelled unverified against policy.
- **Failure modes:** Human stays decision-maker; do not pick "not reportable" to be helpful.

## Workflow

1. Restate facts sourced; list unknowns.
2. Options for the human: gather more facts / treat as complaint only / escalate to RM for reportable assessment / other per policy — **not** a recommended legal conclusion.
3. Checklist of policy questions (who, when, significance) drawn from the supplied policy, else generic `[verify]`.
4. Next-step owners from org profile.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — triage, not a reportable-situation decision

FACTS: [...]
UNKNOWNS: [...]
OPTIONS FOR THE ACCOUNTABLE HUMAN: [...]
POLICY QUESTIONS: [...]
THIS TOOL DOES NOT DECIDE REPORTABILITY
CONFIDENCE: [...]
```

## Worked example

**Input:** SOA issued with a fee table that used the wrong admin fee for 14 clients; discovered internally.

**Excerpt:** Facts as given. Options: quantify affected clients; RM assessment under licensee policy; do not conclude "significant" here. Time-limit `[verify]`.

## Quality checks before delivering

- [ ] No "this is/isn't reportable" conclusion
- [ ] Time limits not invented
- [ ] Owner is a human role

## Propose profile update

When a stable triage checklist surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/compliance/CLAUDE.md`, ask, write only on yes. Only `/compliance:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
