---
name: file-review
description: >
  This skill should be used when the user asks to "review this advice file",
  "loan file checklist", "BID evidence gaps", "compliance file review", or
  wants a draft file run against a licensee checklist. Assists the reviewer;
  does not certify.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "compliance practice"
  review_cadence: "quarterly"
  work_shape: "hypothesis-driven-analysis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# File Review

## When to use

Run a draft advice or loan file against the licensee's checklist (or a generic BID/record-keeping scaffold if none supplied). Gap list for a human reviewer.

## What this skill does not do

- **Does not pass or fail the file as a certified review.**
- **Does not substitute for the relevant provider's or broker's sign-off.**
- **Does not invent missing file notes to close gaps.**

## Preconditions

| Input | If missing |
|---|---|
| File contents (SOA/ROA/BID/notes/disclosures as provided) | Ask; do not partial-certify |
| Licensee checklist | Use generic headings labelled generic; flag |

## Provisional mode

Partial file: record coverage; review only what was read.

## Trust spine

Per `../../references/trust-conventions.md`. For advice files, s961B/s947 elements as **questions**. For credit files, RG 273 cost/options as **questions**.

- **Confidence bands** (`hypothesis-driven-analysis`): High = full file + licensee checklist; Low = partial read flagged.
- **Failure modes:** Reviewer stays decision-maker; do not "fix" the file by drafting fake evidence.

## Workflow

1. Identify regime (advice / credit / both).
2. Read full supplied file; state coverage.
3. Checklist: item | evidenced (cite location) | gap | severity (profile scale).
4. Incomplete-information and conflict flags.
5. Rank blocking gaps. No overall "compliant" stamp.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — gap list, not a clearance

COVERAGE: [...]
CHECKLIST: [...]
BLOCKING GAPS: [...]
NOT CERTIFIED
CONFIDENCE: [...]
```

## Worked example

**Input:** SOA without replacement-product table; fact-find expenses blank; no FSG evidence.

**Excerpt:** Blocking: incomplete expenses (s961B enquiry path). High: s947D table missing if replacement in scope `[review]`. Not certified.

## Quality checks before delivering

- [ ] No pass certificate
- [ ] Citations to file locations
- [ ] Coverage stated

## Propose profile update

When a stable checklist mapping surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/compliance/CLAUDE.md`, ask, write only on yes. Only `/compliance:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs.
