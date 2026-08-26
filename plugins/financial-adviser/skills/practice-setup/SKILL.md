---
name: practice-setup
description: >
  This skill should be used when the user runs
  "/financial-adviser:practice-setup" (with optional --quick, --full, --redo,
  --check-integrations, or --resume), asks to "set up the financial-adviser
  plugin", or wants to configure SOA/CAR templates, APL location, and review
  cadence. Writes the shared org profile and the financial-adviser practice
  profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.1.0"
  owner: "financial-adviser practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — financial-adviser

## When to use

Relevant providers and paraplanners configuring advice-document regime, APL, and review/FDS cadence. Explicit invocation only.

## What this skill does not do

- **Does not draft SOA/ROA/CAR** — writes profiles only.
- **Does not auto-write without confirmation.**
- **Does not decide that the CAR regime applies** — record the licensee's instruction; default remains SOA.

## Preconditions

Per `../../references/practice-setup-framework.md` — detect setup, offer quick/full.

## Provisional mode

Quick mode: licence already in org profile; capture SOA-vs-CAR instruction, APL path, who signs, FDS lead time.

## Trust spine

Structured-aggregation bands; redacted seed SOAs only; explicit confirmation before write; never copy client names into the profile.

## Shared framework

Read `../../references/practice-setup-framework.md` with `financial-adviser` as plugin name.

**Org:** `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md`
**Plugin:** `~/.claude/plugins/config/claude-for-financial-planners/financial-adviser/CLAUDE.md`

## Plugin-specific interview

1. Full mode: 1–2 redacted SOAs or review packs for structure (not content).
2. Advice types in scope.
3. Document regime — SOA default vs CAR only if licensee confirms.
4. Who drafts vs who signs; paraplanning model.
5. APL location and refresh; risk-profile tool name (do not re-score here).
6. Annual review / FDS / ongoing-fee consent lead times.
7. Write profiles; confirm.

## Living profile

Auto-apply this skill only after confirmation; other skills use propose profile update.

## Output format

Summary of org + plugin changes; defaults used; files written on confirmation; standing rule restated.

## Worked example

**Input:** `--quick`, AFSL AR, SOA still in force, APL in FYI, FDS 30 days before anniversary, paraplanner drafts / RP signs.

**Summary excerpt:** Regime SOA; CAR not enabled; FDS lead 30 days; recommendation always RP-authored.

## Quality checks before delivering

- [ ] CAR not enabled unless licensee confirmed
- [ ] Confirmation before write
- [ ] No client PII in profile

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/financial-adviser:fact-find` or `/financial-adviser:soa-draft`.
