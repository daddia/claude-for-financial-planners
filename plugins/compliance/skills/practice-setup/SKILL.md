---
name: practice-setup
description: >
  This skill should be used when the user runs "/compliance:practice-setup"
  (with optional --quick, --full, --redo, --check-integrations, or --resume),
  asks to "set up the compliance plugin", or wants to configure file-review
  checklists, complaint SLAs, and audit-export paths.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.1.0"
  owner: "compliance practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — compliance

## When to use

Compliance managers and responsible managers configuring file-review, complaints, and record-keeping conventions. Explicit invocation only.

## What this skill does not do

- **Does not certify files or decide reportable situations** — writes profiles only.
- **Does not auto-write without confirmation.**
- **Does not replace `/compliance:ai-governance-setup`** for the full REP 798 inventory — records whether one exists.

## Preconditions

Per `../../references/practice-setup-framework.md`.

## Provisional mode

Quick: checklist path, complaints owner, acknowledgement SLA, file-aging days, audit-export folder.

## Trust spine

Structured-aggregation bands; redacted seed reviews only; no client PII in profile.

## Shared framework

Read `../../references/practice-setup-framework.md` with `compliance` as plugin name.

**Org:** `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md`
**Plugin:** `~/.claude/plugins/config/claude-for-financial-planners/compliance/CLAUDE.md`

## Plugin-specific interview

1. Full mode: redacted file-review checklist or complaint acknowledgement.
2. Advice vs credit review split.
3. Severity scale.
4. Complaint IDF → AFCA path; acknowledgement SLA.
5. Who decides reportable situations (name/role only).
6. File-aging threshold; audit-export destination.
7. Write; confirm. Offer `ai-governance-setup` if no inventory.

## Living profile

Auto-apply this skill only after confirmation; other skills use propose profile update.

## Output format

Summary of changes; files written on confirmation.

## Worked example

**Input:** `--quick`, dual AFSL/ACL, FYI checklists, 24-hour complaint ack, 90-day file-aging, RM decides reportable situations.

**Summary excerpt:** Plugin assists reviewer; does not certify. AI inventory still missing → next `ai-governance-setup`.

## Quality checks before delivering

- [ ] Reportable-situation owner is a human role
- [ ] Confirmation before write

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/compliance:file-review` or `/compliance:ai-governance-setup`.
