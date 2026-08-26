---
name: audit-export
description: >
  This skill should be used when the user asks to "export the audit trail",
  "7-year record pack", "what did we rely on for this SOA", "PI defence file",
  or wants a reconstructable pack of inputs, drafts, and approver fields.
  Does not invent an approver.
allowed-tools: Read, Grep, Glob, Write
metadata:
  version: "0.1.0"
  owner: "compliance practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Audit Export

## When to use

Assemble an exportable markdown pack for a matter: inputs, skills invoked this session (and files the user points at), drafts, gaps, approver blank until signed. See `../../references/record-keeping.md`.

## What this skill does not do

- **Does not certify** 7-year completeness of the licensee's whole record system.
- **Does not invent** prompts, outputs, or sign-off that were not in session or supplied.
- **Does not write** until the user confirms the path.

## Preconditions

| Input | If missing |
|---|---|
| Matter identifier the user supplies | Ask — do not invent client codes |
| What to include (this session / named files) | Default this session only |

## Provisional mode

If little is in session: pack will be thin; say so.

## Trust spine

Per `../../references/record-keeping.md` and `trust-conventions.md`. s286 / Instrument 2024/508 are the licensee's obligations — this pack is a reconstruction aid.

- **Confidence bands** (`structured-aggregation`): High = named files + session drafts; Low = session-only fragments.
- **Failure modes:** No fake completeness; PII only as already in the sourced files.

## Workflow

1. List inputs and outputs actually available.
2. Build pack per record-keeping.md.
3. Confirm path (workspace or `~~documents` folder the user names).
4. Write on yes. Approver remains TBD unless the user names who signed.

## Output format

Pack structure in `../../references/record-keeping.md`. Stamp disclaimer.

## Worked example

**Input:** "Export what we used for the Smith SOA draft this afternoon" + client code C-4412.

**Excerpt:** Matter C-4412 `[sourced: user]`. Inputs: fact-find.md, APL extract. Output: soa-draft session. Approver TBD. Written to `audit-C-4412.md` after confirm.

## Quality checks before delivering

- [ ] No invented approver
- [ ] Coverage honest
- [ ] Confirmation before write

## Propose profile update

When a stable export path or pack heading set surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/compliance/CLAUDE.md`, ask, write only on yes. Only `/compliance:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
