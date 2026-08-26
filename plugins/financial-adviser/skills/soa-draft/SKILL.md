---
name: soa-draft
description: >
  This skill should be used when the user asks to "draft an SOA", "draft a
  Statement of Advice", "Client Advice Record", "CAR draft", or "scaffold the
  advice document from this fact-find". Mode-switchable SOA (default) or CAR
  when the licensee confirms. The adviser authors the recommendation and signs.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "financial-adviser practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# SOA / CAR Draft

## When to use

Scaffold a Statement of Advice or, **only if the licensee has confirmed the CAR regime applies to this file**, a Client Advice Record. Pull structure from the fact-find, risk-profile artefact, holdings, APL extracts, and the firm's template. The **relevant provider writes and owns the recommendation and reasoning**.

## What this skill does not do

- **Does not provide personal advice** and does not select products from the APL.
- **Does not certify BID, appropriateness (s961G), or "clear, concise and effective".**
- **Does not assume s961B(2) safe-harbour steps are repealed** — see `../../references/bid-s961b.md`.
- **Does not default to CAR** — SOA unless profile or user confirms CAR.

## Preconditions

| Input | If missing |
|---|---|
| Fact-find / circumstances | Ask; if incomplete, scaffold headings and **refuse recommendation-shaped sections** |
| Advice-document regime | Default SOA; CAR only on confirmation |
| Licensee template if any | Use `../../references/soa-content.md` headings |
| APL / product docs for any product the **adviser names** | `[verify]` / `INPUT NEEDED` — do not pick a product to fill the gap |

## Provisional mode

Incomplete fact-find: produce a **structure-only** draft with incomplete-information warning; leave recommendation blank.

## Trust spine

```
DISCLAIMER / SOURCING / ASSUMPTIONS / NUMBERS / CONFIDENCE / GATE / PROHIBITED
per ../../references/trust-conventions.md
```

- **Confidence bands** (`narrative-synthesis`): High = complete sourced file + adviser-supplied recommendation wording; Medium = complete file, recommendation still blank; Low = incomplete file — structure only.
- **Failure modes:** The adviser stays the decision-maker (`[review]` on every strategy/product line); no invented fees; BID checklist is questions, not a certificate (`../../references/bid-s961b.md`).
- **Escalation:** Replacement of product (s947D), conflicts, tax beyond confirmed QTRP scope, vulnerable client.

## Workflow

1. Read profiles. Confirm **MODE: SOA** or **MODE: CAR [licensee-confirmed]**.
2. Read `soa-content.md` and `bid-s961b.md`.
3. Map s947B/C (or CAR template) headings; fill only sourced facts.
4. Insert BID safe-harbour **checklist for the adviser** — do not tick as passed.
5. Leave **Recommended strategy / products / why** as blank `[review — adviser authors]` unless the user pasted their wording (then quote it as theirs, do not embellish).
6. Tag product facts; never add APL products the adviser did not name.
7. Licensed-human gate before any "file-ready" version. Stamp reviewer note + audit log.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW
MODE: SOA | CAR [licensee-confirmed]
Not personal advice. Relevant provider is the authorising signatory.

[template sections]
RECOMMENDATION / REASONING: [adviser-authored or BLANK]
BID CHECKLIST (s961B(2) — adviser completes): [...]
INCOMPLETE INFORMATION: [...]
AUDIT LOG: [...]
CONFIDENCE: [...]
```

## Worked example

**Input:** Complete fact-find; adviser says "I will recommend remaining with current super and increasing concessional contributions; draft the SOA around that."

**Excerpt:** MODE SOA. Strategy quoted as adviser-supplied `[sourced: user]`. No other products introduced. Fee table `INPUT NEEDED` from licensee schedule. BID checklist all `[review]`.

## Quality checks before delivering

- [ ] No model-selected products
- [ ] CAR only if confirmed
- [ ] Safe-harbour not certified
- [ ] Gate before file-ready

## Propose profile update

When a stable SOA/CAR heading or regime instruction surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/financial-adviser/CLAUDE.md`, ask, write only on yes. Only `/financial-adviser:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Signing is a human action.
