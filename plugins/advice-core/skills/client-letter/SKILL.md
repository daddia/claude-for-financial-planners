---
name: client-letter
description: >
  This skill should be used when the user asks to "draft a client email",
  "annual review letter", "document-request email", "appointment confirmation",
  or "plain-language explanation" for a client. The adviser or broker edits
  and sends; this skill does not send and does not give personal advice.
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
# Client Letter

## When to use

Client-facing comms: appointment/doc-request emails, annual-review invitations, plain-language process explanations. Adviser/broker edits and approves.

## What this skill does not do

- **Does not send** via `~~email` unless the user explicitly confirms after the licensed-human gate **and** destination check.
- **Does not include personal advice, product picks, or lender recommendations.**
- **Does not replace SOA/ROA/BID documents** — for those use `financial-adviser` / `mortgage-broker` skills.

## Preconditions

| Input | If missing |
|---|---|
| Purpose and audience | Ask |
| Facts to include (dates, docs needed, meeting time) | `INPUT NEEDED` — do not invent |
| Practice profile house style | Default plain, professional Australian English |

## Provisional mode

Missing facts: draft with placeholders, **structured first pass**, do not guess a review date or fee.

## Trust spine

- **Confidence bands** (`narrative-synthesis`): High = sourced dates/docs + house style; Medium = purpose only with placeholders; Low = halt if the user asked for a product explanation that would be personal advice — redirect.
- Per `../../references/trust-conventions.md`. **GATE** before treating as ready to send.
- **Failure modes:** If the ask is "explain why this super/loan is right for them" → stop and point at SOA/BID skills; confidentiality/destination check; `[review]` on any fee or rate.
- **Escalation:** Complaint tone from client → `/compliance:complaint-intake`; vulnerability → flag, simplify, do not advise.

## Workflow

1. Classify: operational comms (in scope) vs advice/credit recommendation (out of scope).
2. Read house style.
3. Draft: purpose first; documents/dates as bullets; no product persuasion.
4. Tag every figure; placeholders for unknowns.
5. Pre-send summary + ask for gate confirmation if user wants a send-ready version.

## Output format

```
DRAFT FOR LICENSED HUMAN REVIEW — not sent

PURPOSE: [...]
CHANNEL: [email / letter]
SUBJECT / TITLE: [...]
BODY: [...]
PLACEHOLDERS / INPUT NEEDED: [...]
DO NOT INCLUDE: product or lender recommendation
CONFIDENCE: [...]
```

## Worked example

**Input:** "Email Jane to book her annual review and list the documents we need."

**Excerpt:** Subject: Annual review — documents and times. Body lists docs from profile template; no commentary on current holdings.

## Quality checks before delivering

- [ ] No personal advice or credit assistance
- [ ] No invented dates, fees, or rates
- [ ] Not sent unless gated

## Propose profile update

When a stable letter structure or sign-off surfaces, **propose a profile update** to `~/.claude/plugins/config/claude-for-financial-planners/advice-core/CLAUDE.md`, ask, write only on yes. Only `/advice-core:practice-setup` auto-applies a full profile write.

## Outputs

Follows plugin `CLAUDE.md` § Outputs. Sending is a human action.
