---
name: ai-governance-setup
description: >
  This skill should be used when the user asks to "set up AI governance",
  "REP 798 inventory", "AI use policy template", "human in the loop map",
  or "ASIC AI questions for our licensee". Writes an AI inventory draft
  after confirmation. Does not certify adequacy.
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
# AI Governance Setup

## When to use

Turn ASIC REP 798's 11 questions into an inventory and accountability map, including **this marketplace** as a third-party generative-AI use case. Template AI-use policy for compliance to finish.

## What this skill does not do

- **Does not certify** that arrangements are adequate for ASIC.
- **Does not auto-write without confirmation.**
- **Does not make this product a digital advice provider** — inventory must record the assist-a-human boundary (RG 255).

## Preconditions

| Input | If missing |
|---|---|
| Who is accountable (role) | Ask |
| Other AI tools in the practice (Claras, Copilot, etc.) | Record "this plugin only" if that is the answer |

## Provisional mode

Quick: inventory this plugin + named others; humans-in-the-loop; monitoring cadence; data-handling pointer from org profile.

## Trust spine

Per `../../references/ai-governance-rep798.md` and `trust-conventions.md`. Consumer-harm lens, not only efficiency.

- **Confidence bands** (`structured-aggregation`): High = walkthrough of 11 questions; Medium = quick inventory.
- **Failure modes:** Third-party models get the same governance fields as internal; do not tick ethics principles as "done".

## Workflow

1. Interview the 11 questions (quick: 1, 4, 7, 9, 10).
2. Draft inventory table + human-accountability points + monitoring cadence.
3. Draft AI-use policy skeleton: purpose; prohibited uses (no autonomous personal advice/credit assistance); HITL; records; vendors; review cadence.
4. Show summary; write on confirmation to `~/.claude/plugins/config/claude-for-financial-planners/compliance/ai-inventory.md` (create dirs). Also **propose** an org-profile pointer to that path.
5. Do not write plugin templates.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — governance artefact, not an ASIC clearance

INVENTORY: [...]
ACCOUNTABILITY: [...]
POLICY SKELETON: [...]
FILES TO WRITE ON CONFIRMATION: [...]
```

## Worked example

**Input:** Practice uses this plugin + Microsoft Copilot; principal accountable; quarterly review.

**Excerpt:** Two use cases; both HITL; prohibited: autonomous SOA/lender pick. Inventory path recorded. Not certified adequate.

## Quality checks before delivering

- [ ] Confirmation before write
- [ ] RG 255 boundary explicit
- [ ] This plugin listed as third-party

## Propose profile update

This skill may write `ai-inventory.md` after confirmation (artefact). For the practice profile pointer, **propose** the CLAUDE.md/org-profile diff, ask, write only on yes — except the inventory file itself when the user confirmed the summary. Only `/compliance:practice-setup` auto-applies a **full** practice-profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
