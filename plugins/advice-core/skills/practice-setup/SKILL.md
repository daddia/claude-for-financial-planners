---
name: practice-setup
description: >
  This skill should be used when the user runs "/advice-core:practice-setup"
  (with optional --quick, --full, --redo, --check-integrations, or --resume),
  asks to "set up advice-core", "configure my advice practice", or "teach Claude
  my file-note and letter style" for the first time. Writes the shared licensee
  org profile and the advice-core practice profile.
allowed-tools: Read, Grep, Glob, Write
disable-model-invocation: true
metadata:
  version: "0.1.0"
  owner: "advice-core practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: artefact-writer
  output_class: "structured-data"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Practice Setup — advice-core

## When to use

Run before any other advice-core skill produces tailored output. Explicit invocation only. First plugin set up also writes the shared licensee org profile reused by `financial-adviser`, `mortgage-broker`, and `compliance`.

## What this skill does not do

- **Does not produce advice, file notes, or letters** — configures profiles other skills read.
- **Does not auto-write without confirmation** — summary first, write on explicit yes.
- **Does not modify plugin templates** in the repo — writes user config only.
- **Does not complete REP 798 AI governance** — point at `/compliance:ai-governance-setup` for the full inventory.

## Preconditions

| Input | If missing |
|---|---|
| User intent (quick/full/redo/check-integrations/resume) | Detect setup; offer quick vs full |
| Write access to config path | Explain path on confirmed write |

## Provisional mode

Quick mode or complete org profile: skip answered org questions; use "no strong preference" for unset plugin fields.

## Trust spine

- **Confidence bands** (`structured-aggregation`): High = confirmed summary + seed review in full mode; Medium = quick with defaults; Low = paused — resume file only.
- **Failure modes:** Captures user conventions; does not impose a licensee template; redacts client PII from seed docs before writing the profile; explicit confirmation before write.
- **Escalation:** Legacy profile paths → offer migration; install scope blocks reads → explain per framework.

## Shared framework

Read and follow `../../references/practice-setup-framework.md` with `advice-core` as the plugin name.

**Org profile:** `~/.claude/plugins/config/claude-for-financial-planners/org-profile.md`
**Plugin profile:** `~/.claude/plugins/config/claude-for-financial-planners/advice-core/CLAUDE.md`

## Plugin-specific interview

After the org layer is satisfied:

1. **Quick vs full** — full mode reviews 2–3 redacted file notes, letters, or meeting packs for tone and structure.
2. **Role and artefacts** — adviser, broker, paraplanner, assistant; which drafts this plugin will produce most.
3. **File-note and meeting conventions** — licensee template vs skill default; recording-consent practice.
4. **CRM hygiene** — which fields must never be blank; source hierarchy when CRM and notes disagree.
5. **Client-letter and marketing review chain** — who edits before send / publish.
6. **Write profiles** per framework; no blanks — use "no strong preference" or "see org profile".
7. **Confirm and summarize.** Restate: every later output is a draft for licensed human review.

## Living profile

- **Auto-apply:** this skill only, after confirmation.
- **Propose profile update:** all other skills.

## Output format

```
ORG PROFILE CHANGES: [...]
PLUGIN PROFILE CHANGES: [role, templates, CRM fields, review chain]
DEFAULTS USED: [...]
FILES WRITTEN: [on confirmation]
STANDING RULE: drafts only — licensed human signs
```

## Worked example

**Input:** `--quick`, dual advice/broking practice, XPLAN + Mercury, licensee file-note template, principal reviews letters before send.

**Summary excerpt:** Org: dual AFSL/ACL, XPLAN for advice / Mercury for broking. Plugin: file-note follows licensee template; letters principal-gated; CRM must have objectives, income, and consent flags.

## Quality checks before delivering

- [ ] Framework startup rules followed
- [ ] Explicit confirmation before write
- [ ] No client PII copied into the profile
- [ ] No strong preference recorded where user deferred

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/advice-core:meeting-prep`, `/advice-core:file-note`, or `--check-integrations`. Offer `/compliance:ai-governance-setup` if the org profile has no AI inventory.
