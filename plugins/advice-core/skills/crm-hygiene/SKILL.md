---
name: crm-hygiene
description: >
  This skill should be used when the user asks to "update the CRM from these
  notes", "what's missing on this client record", "structure this intake for
  XPLAN / Mercury / AdviserLogic", or wants draft CRM field updates from a
  fact-find or file note for human confirmation.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "advice-core practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# CRM Hygiene

## When to use

Turn intake forms, meeting notes, or emails into a **proposed** CRM field list: values to set, blanks to flag. Human confirms before anything is entered. V1 does not write to `~~crm` (no first-party XPLAN/aggregator MCP).

## What this skill does not do

- **Does not write to the CRM** or lodgement system.
- **Does not invent field values** to make the record look complete.
- **Does not change advice or credit recommendations.**

## Preconditions

| Input | If missing |
|---|---|
| Source notes / intake / file note | Ask |
| CRM field list or "must never be blank" from profile | Use a generic identity / contact / objectives / consent / existing-product set and mark it as generic |
| Practice profile | Flag setup |

## Provisional mode

Unknown CRM schema: output a generic table and ask the user to map columns.

## Trust spine

- **Confidence bands** (`structured-aggregation`): High = licensee field list + sourced values; Medium = generic fields; Low = notes too thin — gap list only.
- Per `../../references/trust-conventions.md`. Every proposed value `[sourced:]` to the note.
- **Failure modes:** Support not advice; PII — propose only fields the user asked to structure; no silent fill of TFN, ID numbers, or income.
- **Escalation:** Conflicting values (email vs CRM) → show both, do not pick.

## Workflow

1. Read org source-hierarchy and advice-core "must never be blank" fields.
2. Extract candidate values from the source.
3. Table: field | proposed value | source | status (set / confirm / missing).
4. Flag conflicts and sensitive fields (TFN, ID, health) as **human-enter only**.
5. Completeness check against must-never-be-blank.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — proposed CRM updates, not applied

FIELD | PROPOSED VALUE | SOURCE | STATUS
...
MISSING MUST-HAVE FIELDS: [...]
CONFLICTS: [...]
DO NOT AUTO-ENTER: [TFN / ID / health / other sensitive]
CONFIDENCE: [...]
```

## Worked example

**Input:** Intake PDF with mobile and email; income left blank; CRM already has a different mobile.

**Excerpt:** Mobile CONFLICT `[sourced: intake]` vs `[sourced: CRM]` — human picks. Income MISSING. Email SET from intake.

## Quality checks before delivering

- [ ] No invented values
- [ ] Conflicts shown, not resolved
- [ ] Sensitive fields not inlined in `~~chat`

## Propose profile update

When a stable CRM field list or must-never-be-blank set surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/advice-core/CLAUDE.md` (systems of record → org profile), ask, write only on yes. Only `/advice-core:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Human applies updates in `~~crm`.
