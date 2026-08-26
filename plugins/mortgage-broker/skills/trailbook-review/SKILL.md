---
name: trailbook-review
description: >
  This skill should be used when the user asks to "review the trail book",
  "repricing opportunities", "refinance watchlist", "fixed-rate expiry list",
  or wants a book-level scan from a supplied trail/expiry extract. Does not
  contact clients or recommend a refinance.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "mortgage-broker practice"
  review_cadence: "quarterly"
  work_shape: "governance-tracking"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Trail Book Review

## When to use

From a **user-supplied** trail-book / expiry / rate extract: flag upcoming fixed-rate ends, possible review conversations. Internal watchlist.

## What this skill does not do

- **Does not recommend refinancing** a named client (that is new credit assistance — needs needs-analysis + BID).
- **Does not scrape `~~crm` for the whole book** unless connected and asked; V1 has no aggregator MCP — require an extract.
- **Does not email the book.**

## Preconditions

| Input | If missing |
|---|---|
| Spreadsheet or CRM extract with dates/rates as the practice uses | Ask; do not invent clients |
| Lead time from profile | Default 90 days to fixed expiry if unset |

## Provisional mode

Incomplete columns: flag; do not guess rates.

## Trust spine

Per `../../references/trust-conventions.md`. Market-rate comparisons `[verify]` unless sourced.

- **Confidence bands** (`governance-tracking`): High = dated extract; Low = no extract — halt.
- **Failure modes:** Do not present a "save $X" as a client recommendation; incentive gaming — do not sort solely by trail income.

## Workflow

1. Parse extract; state coverage.
2. Table: matter code | event (expiry/review) | date | days | **conversation flag** (not "refinance them").
3. Exclude rows with insufficient data.
4. Next: human decides who to call; then `needs-analysis` per client.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — internal watchlist, not credit assistance

COVERAGE: [rows read]
WATCHLIST: [...]
NOT A REFINANCE RECOMMENDATION
CONFIDENCE: [...]
```

## Worked example

**Input:** 40-row export; 6 fixed expiries inside 90 days.

**Excerpt:** Six conversation flags. No $ savings invented. Sort by date, not trail.

## Quality checks before delivering

- [ ] No invented clients or savings
- [ ] Not sorted to maximise trail
- [ ] Not client-facing

## Propose profile update

When a stable lead time or export-column map surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/mortgage-broker/CLAUDE.md`, ask, write only on yes. Only `/mortgage-broker:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Watcher: `trailbook-opportunity-watcher`.
