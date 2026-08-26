---
name: fact-find
description: >
  This skill should be used when the user asks to "structure a fact-find",
  "what's missing from this client fact find", "organise discovery notes",
  or needs a gap-led fact-find pack from intake notes before SOA work.
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
# Fact Find

## When to use

Structure client discovery for personal advice: objectives, financial situation, needs, existing products, risk-profile status. Gap list for the adviser — not a completed picture invented by the model.

## What this skill does not do

- **Does not produce an SOA or a recommendation.**
- **Does not complete a risk profile or product choice.**
- **Does not treat blanks as zeros.**

## Preconditions

| Input | If missing |
|---|---|
| Notes, intake, or CRM extract | Ask |
| Practice / org profile | Use generic retail fact-find headings; flag setup |

## Provisional mode

Thin notes: output headings + `INPUT NEEDED`; **structured first pass**.

## Trust spine

- **Confidence bands** (`structured-aggregation`): High = comprehensive sourced notes; Medium = partial; Low = headings only.
- Incomplete information must be loud — this feeds s961B enquiry/warning (`../../references/bid-s961b.md`).
- **Failure modes:** Support not advice; PII minimisation in chat; do not infer "comfortable with growth" from casual chat.
- **Escalation:** Vulnerability, family-law, bankruptcy, or tax-agent issues → flag for the human / TPB-competent reviewer.

## Workflow

1. Map notes into: identity & consent; objectives; income/expenses; assets/liabilities; super/insurance/estate; existing advice/products; risk-profile artefact (present/stale/missing); time horizon; constraints.
2. Tag every figure.
3. List incomplete-information items that would block appropriate personal advice.
4. Do not fill from "typical Australian household" knowledge.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — fact-find structure, not advice

SECTIONS: [heading | sourced facts | INPUT NEEDED]
RISK PROFILE ARTEFACT: [present + date | stale | missing]
INCOMPLETE INFORMATION (s961B enquiry/warning path): [...]
NEXT: adviser completes gaps before /financial-adviser:soa-draft
CONFIDENCE: [...]
```

## Worked example

**Input:** Discovery notes with salary and super balance; no expenses; no insurance schedule; risk profile 2019.

**Excerpt:** Expenses INPUT NEEDED. Risk profile stale `[review]`. Incomplete information list at top — do not draft SOA yet.

## Quality checks before delivering

- [ ] No product recommendation
- [ ] Blanks are blanks
- [ ] Incomplete-information block present

## Propose profile update

When a stable fact-find heading set surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/financial-adviser/CLAUDE.md`, ask, write only on yes. Only `/financial-adviser:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `soa-draft` only when the adviser says the file is complete enough.
