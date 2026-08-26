---
name: file-note
description: >
  This skill should be used when the user asks to "write a file note", "turn
  this transcript into a note", "meeting notes for the file", or provides a
  consented recording/transcript and wants a structured, reviewable file note.
  Records what happened; it does not advise.
allowed-tools: Read, Grep, Glob
metadata:
  version: "0.1.0"
  owner: "advice-core practice"
  review_cadence: "quarterly"
  work_shape: "narrative-synthesis"
  permission_tier: advisory
  output_class: "draft-for-review"
  sourcing_policy: "volatile-facts-must-be-sourced"
---
# File Note

## When to use

Post-meeting file note from a **consented** transcript, recording summary, or handwritten notes. Both advice and broking.

## What this skill does not do

- **Does not turn discussion into personal advice or a lender recommendation.**
- **Does not invent attendance, consent, or figures** that are not in the source.
- **Does not file to `~~crm`** — drafts the note; human pastes or confirms.

## Preconditions

| Input | If missing |
|---|---|
| Source (transcript, notes, or recording summary) | Ask; do not fabricate a meeting |
| Evidence of recording/transcript consent | If a recording/transcript is used and consent is not evidenced, halt and ask |
| Practice profile file-note template | Use the default structure below |

## Provisional mode

Partial transcript: note coverage (`Read: [range]`) and label **structured first pass**. Do not smooth gaps into a complete story.

## Trust spine

- **Confidence bands** (`narrative-synthesis`): High = full consented transcript + template; Medium = notes only; Low = fragmentary notes — flag, don't narrate.
- Per `../../references/trust-conventions.md`. Include **AUDIT LOG** fields (inputs, skill, date; approver blank).
- **Failure modes:** Support not advice; confidentiality of transcript; accountability — `[review]` on any inference beyond the source; analytical rigor — quotes or timestamps for material client statements.
- **Escalation:** Complaint language, vulnerability, or "please recommend X" from the client → flag for the human; do not answer in the note as if advice were given.

## Workflow

1. Confirm consent if the source is a recording/transcript.
2. Read practice profile template.
3. Extract: attendees, date, purpose, client statements (objectives, circumstances), information provided (general vs anything that looks like personal advice — flag), actions, documents requested.
4. Separate **client said** / **adviser or broker said** / **actions**.
5. Do not upgrade chat into a strategy or product choice.
6. Stamp disclaimer + incomplete-information + audit log.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW

MATTER / CLIENT CODE: [...]
DATE / ATTENDEES / PURPOSE: [...]
CONSENT (recording/transcript): [sourced | not applicable | INPUT NEEDED]
CLIENT STATEMENTS: [...]
INFORMATION PROVIDED (non-advice / flag if advice-shaped): [...]
ACTIONS / NEXT STEPS (owners): [...]
INCOMPLETE INFORMATION: [...]
AUDIT LOG: inputs | skill: file-note | date | approver: TBD
CONFIDENCE: [...]
```

## Worked example

**Input:** 22-minute consented transcript; client asked "which super fund is best"; adviser said they would complete a fact-find first.

**Excerpt:** CLIENT STATEMENTS: wants lower fees and simpler paperwork. INFORMATION PROVIDED: no product named. `[review]` client asked for a recommendation — not given in meeting.

## Quality checks before delivering

- [ ] Consent handled
- [ ] No invented quotes or numbers
- [ ] Advice-shaped moments flagged, not completed

## Propose profile update

When a stable convention surfaces (file-note headings, consent wording), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-financial-planners/advice-core/CLAUDE.md`, ask, write only on yes. Only `/advice-core:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Next: `/advice-core:crm-hygiene` or a profession skill (`fact-find`, `needs-analysis`).
