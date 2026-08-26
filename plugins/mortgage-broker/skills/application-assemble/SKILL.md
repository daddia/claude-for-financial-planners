---
name: application-assemble
description: >
  This skill should be used when the user asks to "application checklist",
  "what's missing for ApplyOnline", "assemble the loan pack", "docs for
  lodgement", or wants a document-collection checklist for a credit
  application. Does not lodge.
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
# Application Assemble

## When to use

Checklist for consumer-credit application assembly: docs collected vs required, gaps, e-sign pack contents. Human lodges (ApplyOnline or other). No first-party lodgement MCP in V1.

## What this skill does not do

- **Does not lodge**, e-sign, or submit to a lender.
- **Does not certify ID verification, Equifax, or responsible lending.**
- **Does not fill application forms with invented data.**

## Preconditions

| Input | If missing |
|---|---|
| Lender/product the **broker has chosen** | Ask — do not choose |
| Doc list (licensee/lender) or generic residential checklist labelled generic | Use generic + flag |
| What is already on file | Ask |

## Provisional mode

Unknown lender doc list: generic checklist, **structured first pass**.

## Trust spine

Per `../../references/trust-conventions.md`. RG 209 verification is the licensee's process.

- **Confidence bands** (`structured-aggregation`): High = lender doc list + file inventory; Low = generic list.
- **Failure modes:** No silent completeness; ID/TFN not echoed into `~~chat`.

## Workflow

1. Confirm the broker has chosen the lender (else stop and point at comparison/BID skills).
2. Checklist: item | status | source | blocker for lodgement.
3. E-sign pack list if `~~e-signature` in profile.
4. Gate: this is not lodgement.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — assembly checklist, not lodged

LENDER (broker-chosen): [...]
DOCS: [item | have/missing]
BLOCKERS: [...]
DO NOT LODGE FROM THIS TOOL
CONFIDENCE: [...]
```

## Worked example

**Input:** Broker chose lender A; payslips on file; no council rates; ID done in CRM.

**Excerpt:** Rates notice missing — blocker. ID "present in CRM" `[sourced: user]` — do not re-attach PII here.

## Quality checks before delivering

- [ ] Lender not selected by the model
- [ ] Not described as lodged
- [ ] Sensitive IDs not pasted

## Propose profile update

When a stable doc checklist surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/mortgage-broker/CLAUDE.md`, ask, write only on yes. Only `/mortgage-broker:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Lodgement is a human action.
