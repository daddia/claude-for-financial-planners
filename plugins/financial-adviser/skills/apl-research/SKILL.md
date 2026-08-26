---
name: apl-research
description: >
  This skill should be used when the user asks to "research this product
  against the APL", "summarise this PDS/TMD", "investment research note",
  "sector commentary for the file", or wants general (not personal) product
  research constrained to the Approved Product List.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "financial-adviser practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# APL Research

## When to use

General product/market notes **against the firm's APL** (or a user-supplied extract). For the adviser's working file — not a client recommendation.

## What this skill does not do

- **Does not recommend a product to a client** or imply it is appropriate for a named client.
- **Does not add off-APL products** unless the user explicitly asks for a "not on APL — do not recommend" comparison, clearly labelled.
- **Does not coach TMD gating.**

## Preconditions

| Input | If missing |
|---|---|
| Product name(s) and APL extract or confirmation on-APL | Ask; if APL missing, stop product-inclusion claims |
| PDS/TMD/research PDF or URL content in session | Tag `[verify]` / `INPUT NEEDED`; do not invent features |

## Provisional mode

Model-only product knowledge: **structured first pass**, every feature `[model knowledge — verify]`, not for the client file.

## Trust spine

Per `../../references/trust-conventions.md` and `../../references/ddo-tmd.md`. Currency: prefer documents in session over training data.

- **Confidence bands** (`structured-aggregation`): High = APL + current PDS/TMD in session; Low = name only.
- **Failure modes:** General commentary vs personal advice; no silent off-APL expansion.

## Workflow

1. Confirm on-APL `[sourced]`.
2. Summarise features, fees, risks, TMD snapshot from supplied docs.
3. Separate **general** market/sector commentary with `[verify]`.
4. Explicit line: "Not personal advice; not a recommendation for [client]."

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — general research, not personal advice

PRODUCT: [...]
APL STATUS: [on-list sourced | not on list | unknown]
FEATURES / FEES / RISKS: [sourced or verify]
TMD SNAPSHOT: [or INPUT NEEDED]
NOT FOR CLIENT RECOMMENDATION
CONFIDENCE: [...]
```

## Worked example

**Input:** Adviser uploads PDS + TMD for an APL managed fund; wants a one-pager.

**Excerpt:** On-APL `[sourced: APL extract]`. MER `[sourced: PDS p12]`. TMD retail clients with 5+ year horizon `[sourced: TMD]`. No client named.

## Quality checks before delivering

- [ ] Not personalised to a client's circumstances
- [ ] APL status explicit
- [ ] No gating questions for a consumer

## Propose profile update

When a stable research-note template surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/financial-adviser/CLAUDE.md`, ask, write only on yes. Only `/financial-adviser:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
