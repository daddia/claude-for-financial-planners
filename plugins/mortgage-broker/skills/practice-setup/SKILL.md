---
name: practice-setup
description: >
  This skill should be used when the user runs
  "/mortgage-broker:practice-setup" (with optional --quick, --full, --redo,
  --check-integrations, or --resume), asks to "set up the mortgage-broker
  plugin", or wants to configure lender panel, aggregator CRM, BID template,
  and trail-book cadence.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.1.0"
  owner: "mortgage-broker practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — mortgage-broker

## When to use

Brokers and credit representatives configuring panel, BID file conventions, and lodgement path. Explicit invocation only.

## What this skill does not do

- **Does not compare lenders or draft BID** — writes profiles only.
- **Does not auto-write without confirmation.**

## Preconditions

Per `../../references/practice-setup-framework.md`.

## Provisional mode

Quick: aggregator, panel location, default comparison count, who signs BID, NCCP-vs-commercial boundary.

## Trust spine

Structured-aggregation bands; redacted seed BID notes only; no client PII in profile.

## Shared framework

Read `../../references/practice-setup-framework.md` with `mortgage-broker` as plugin name.

**Org:** `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md`
**Plugin:** `~/.claude/plugins/config/claude-for-financial-planners/mortgage-broker/CLAUDE.md`

## Plugin-specific interview

1. Full mode: 1–2 redacted BID file notes or comparison worksheets.
2. Credit types (consumer vs commercial).
3. Aggregator / CRM / ApplyOnline / serviceability tool (Quickli etc. — this plugin does not replace them).
4. Lender panel location; how many lenders to compare as a default (must be more than one for NCCP BID work).
5. BID template; who authors the recommendation.
6. Trail-book / expiry lead times.
7. Write; confirm.

## Living profile

Auto-apply this skill only after confirmation; other skills use propose profile update.

## Output format

Summary of changes; files written on confirmation; standing rule restated.

## Worked example

**Input:** `--quick`, Connective Mercury, panel in SharePoint, compare at least three consumer lenders, broker signs BID, 60-day expiry watch.

**Summary excerpt:** NCCP residential only for BID skills; commercial out of scope; three-lender default; no ApplyOnline MCP in V1.

## Quality checks before delivering

- [ ] Commercial vs NCCP recorded
- [ ] Confirmation before write
- [ ] No client PII in profile

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/mortgage-broker:needs-analysis`.
