---
name: meeting-prep
description: >
  This skill should be used when the user asks to "prep for this client meeting",
  "build a briefing pack", "what should I cover in the fact-find", or needs a
  pre-meeting pack from CRM notes, prior file, and calendar. Assembles an
  internal briefing; it does not advise the client.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "advice-core practice"
  review_cadence: "quarterly"
  work_shape: "structured-aggregation"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# Meeting Prep

## When to use

Pre-meeting briefing for an adviser or broker: what is already on file, what is missing, suggested agenda. Internal only.

## What this skill does not do

- **Does not produce personal advice or credit assistance** for the client.
- **Does not run the meeting or fill the fact-find as if the client had answered.**
- **Does not replace `/financial-adviser:fact-find` or `/mortgage-broker:needs-analysis`** — those structure capture during/after the meeting.

## Preconditions

| Input | If missing |
|---|---|
| Practice profile | Default generic agenda; flag `/advice-core:practice-setup` |
| Client context (CRM extract, prior file, or notes) | Ask for a paste or `~~crm` / `~~documents` pointer |
| Meeting type and date | Ask; `~~calendar` if connected |

## Provisional mode

Thin file: produce a gap-led pack labelled **structured first pass**; do not invent history.

## Trust spine

- **Confidence bands** (`structured-aggregation`): High = CRM + prior file + calendar in session; Medium = notes only; Low = name and meeting type only — gap list, not a briefing that looks complete.
- **SOURCING / ASSUMPTIONS / NUMBERS / CONFIDENCE / GATE** — per `../../references/trust-conventions.md`. This output is internal; still stamp the standing disclaimer.
- **Failure modes:** Support not advice; client confidentiality — do not post the pack to `~~chat` unless asked; no invented balances or "likely objectives".
- **Escalation:** Vulnerable-client flags, complaints on file, or incomplete ID/consent → surface for the human before the meeting.

## Workflow

1. Read org + advice-core practice profiles.
2. Gather: prior file, CRM extract, last file note, open actions, `~~calendar` context.
3. MECE gap list: identity/consent, objectives, financial situation, existing products/loans, documents still needed.
4. Draft internal agenda (questions to ask — not answers to give).
5. Tag every figure; `INPUT NEEDED` for blanks.
6. Completeness check before output.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — internal briefing, not client advice

CLIENT / MATTER: [...]
MEETING: [type, date, attendees]
ON FILE (sourced): [...]
GAPS / INCOMPLETE INFORMATION: [...]
SUGGESTED AGENDA (questions, not recommendations):
1. ...
DOCUMENTS TO REQUEST: [...]
WATCH-OUTS: [complaints, vulnerability, conflicts — if any]
CONFIDENCE: [defensible draft | structured first pass]
```

## Worked example

**Input:** Annual review next Tuesday; CRM shows last SOA 14 months ago; FDS due in 3 weeks; risk profile dated 2022.

**Excerpt:** GAPS: risk profile stale `[review]`; FDS deadline in 21 days `[sourced: CRM]`. AGENDA: confirm objectives unchanged; do not preview product switches.

## Quality checks before delivering

- [ ] No recommendation-shaped language
- [ ] Every figure tagged or `INPUT NEEDED`
- [ ] Agenda is questions, not answers

## Propose profile update

When a stable convention surfaces (meeting-pack sections, required CRM fields), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-financial-planners/advice-core/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask, write only on yes. Only `/advice-core:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: after the meeting, `/advice-core:file-note`.
