# Trust Conventions — Licensed-human review spine

Advice and credit outputs — file notes, SOA/ROA/CAR drafts, lender comparisons, BID rationales, marketing copy — go out under a registered relevant provider's or licensed broker's name. This reference is the marketplace-wide **trust spine**: how to tag what you know, surface what you assume, refuse to fabricate inputs, calibrate confidence honestly, and **hard-gate anything resembling personal advice or credit assistance** behind a licensed human.

This file is the canonical full version. Consequential skills carry a condensed inline block of the same rules. Canonical copy lives in `plugins/advice-core/references/`; other plugins and `plugins/references/` hold identical copies.

**Not legal advice. Not personal advice. Not credit assistance.** These conventions make drafts safer to review; they do not replace professional judgment, licensee sign-off, or legal/compliance review. Only a registered relevant provider (Corporations Act) or a licensed broker / credit representative (NCCP) can provide personal advice or credit assistance.

**Not a digital advice provider.** This marketplace assists a licensed human. It does not itself provide digital financial product advice under ASIC RG 255. Skills must never generate client-facing personal advice or a lender recommendation without the human deciding, editing, and signing.

---

## 1. Standing disclaimer

Every client-facing or file-bound draft must open with (or sit under) this stamp:

```
DRAFT FOR LICENSED HUMAN REVIEW
Not personal advice. Not credit assistance. Not a product or lender recommendation.
The licensed adviser or broker is the authorising signatory.
Do not send, lodge, file, or rely on this output until a registered relevant
provider or licensed broker has reviewed, edited, and signed it.
```

Internal working notes (meeting-prep briefings for the adviser, CRM field-gap lists) still carry the stamp when they contain client facts or figures.

---

## 2. Source and provenance tagging

Every product fact, lender-policy claim, rate, fee, legislated threshold, and dollar amount must carry explicit provenance. Untagged numbers read as verified when they may not be.

### Tags

| Tag | When to use |
| --- | --- |
| `[sourced: <where>]` | The figure or claim comes from a document, dataset, URL, CRM extract, licensee policy, APL, lender guide, or other traceable input the user or a connected tool provided. `<where>` is specific enough to find again. |
| `[verify]` | A factual claim the reader must confirm against a primary source before relying on it. Use on **model-only numbers** — figures from training knowledge or session inference without a traceable input. |
| `[unverified — from training data, needs a real source]` | Long form of `[verify]` when the figure is plausible from general knowledge but was **not** grounded in this session. |
| `[model knowledge — verify]` | Same gate as `[verify]`, with provenance named as training knowledge. |
| `[review]` | A judgment the licensed human must make — strategy, product/lender selection, BID conclusion, TMD alignment call. Not a factual gap. |

### Rules

- Tag **at the point of use** — inline on the number or claim.
- One tag per material claim.
- **Do not upgrade** `[unverified — …]` to `[sourced: …]` without new evidence in the session.
- Prefer connected authoritative sources (licensee APL, current lender policy PDF, CRM extract) over model knowledge.
- Qualitative claims that would change a recommendation ("this product is in target market," "this loan is cheaper," "the client is in a position to…") get the same treatment as numbers.

---

## 3. Assumptions surfaced

Advice and credit files rest on assumptions (completeness of the fact-find, currency of lender policy, risk-profile validity, serviceability inputs). Load-bearing ones must be visible **before** the reader reaches any recommendation-shaped language.

### Load-bearing assumptions

An assumption is **load-bearing** when the draft's structure, comparison, or suggested wording would materially change if the assumption were wrong. Examples: incomplete fact-find, stale risk profile, unverified income, assumed LVR, assumed owner-occupier vs investor, assumed existing product remains on APL.

### Required block

At the **top of the output** (immediately after the standing disclaimer):

```
LOAD-BEARING ASSUMPTIONS:
- [assumption] — if wrong: [what changes]
- …
INCOMPLETE INFORMATION (s961B / RG 273):
- [what is missing that a competent reviewer would need]
```

If information is incomplete, **surface the warning obligation** — do not paper over gaps. For advisers, incomplete information triggers the s961B warning path; for brokers, RG 273 warns against one-size-fits-all processes and prioritises cost/affordability.

### Rules

- **Flag, don't fix** — if an assumption is unstated, name it; do not silently pick a convenient value.
- Distinguish **confirmed** vs **unconfirmed**.
- If there are no load-bearing assumptions, say so explicitly.

---

## 4. Numbers provenance — flag, never invent

Never invent a plausible-looking rate, fee, serviceability result, portfolio value, or legislated threshold.

### Rules

- If a number is **required** and **not provided**, flag `INPUT NEEDED: [what]` — do not fill with a round number or "typical" lender figure unless tagged `[unverified — …]` and clearly marked as a discussion placeholder, never as the basis of a recommendation.
- **Derived numbers** inherit the uncertainty of their inputs. Show the math when material.
- **Precision honesty** — do not imply false accuracy from rough inputs.
- Lender-policy claims and product facts default to `[verify]` unless sourced to a current primary document in this session.

---

## 5. Confidence calibration

| Label | Meaning |
| --- | --- |
| **Defensible draft** | Grounded in user-provided or session-sourced evidence; assumptions stated; material claims tagged; a licensed reviewer could explain this with the cited inputs. Still a draft — not signed advice. |
| **Structured first pass** | Shape and logic are sound, but material numbers, policy claims, or assumptions still depend on unverified or missing inputs. Useful for working sessions, not for the client file without further work. |

### Rules

- Default to **structured first pass** when any load-bearing number or claim is `[unverified — …]` or `INPUT NEEDED`.
- Never label output as **personal advice**, **credit assistance**, or a **recommendation to the client**.
- The overall label is the **weakest** link.

---

## 6. Licensed-human gate

The irreversible action in this domain is **this went to the client, onto the advice/credit file, or into a lodgement as if a licensed person had authorised it.**

### When the gate applies

Before producing a **final** version of any of the following, **stop and confirm**:

- SOA, ROA, or Client Advice Record (CAR) draft intended for the client file
- Credit BID rationale / "why this loan" file note intended for the loan file
- Lender or product comparison the broker/adviser will show a client
- Client-facing letter that explains a strategy, product, or loan
- Marketing copy that will be published
- Anything to be lodged (ApplyOnline, e-sign pack) or filed as a record

Working drafts, internal prep packs, and "for the adviser/broker only" versions do **not** require the gate — but they still carry the standing disclaimer, assumptions, sourcing tags, and confidence labels.

### Gate flow

1. **Present a pre-final summary** — what the draft contains, what remains `[unverified — …]` or `INPUT NEEDED`, and the current confidence label.
2. **Ask explicitly** — e.g. "Confirm you want the file-ready draft with the sourcing gaps noted below? You remain the authorising signatory. I will not treat this as sent, lodged, or signed."
3. **Only after confirmation**, produce the file-ready draft and stamp the **reviewer note**:

```
REVIEWER NOTE (licensed-human gate):
- Confirmed by: [user / role if stated]
- Date: [session date]
- Confidence: [defensible draft | structured first pass]
- Authorising signatory: the licensed adviser / broker — not this tool
- Not verified in this session: [list]
- Reviewer action: [what the human must verify, edit, and sign before send/lodge/file]
```

If the user confirms despite gaps, the reviewer note records that — it does not erase the gaps.

### Hard prohibitions

- Do **not** autonomously select a product or lender and present it to a client as a recommendation.
- Do **not** finalise an SOA/CAR/credit rationale as if it were signed.
- Do **not** coach a client through TMD gating questions.
- Do **not** treat a model-produced "best loan" or "recommended strategy" as the human's decision.

---

## 7. Audit trail

AFS licensees must keep financial records for **7 years** (Corporations Act s286). Personal-advice record-keeping is governed by RG 175 and ASIC Instrument 2024/508 (notional s912G(7)). Prompts, outputs, and interaction metadata are business records for AFSL/ACL audits and PI/complaints defence.

Every consequential output should make it easy to record:

- Inputs relied on (files, CRM extracts, transcripts, policy PDFs)
- Material prompts / skill invoked
- Model output (the draft)
- Who reviewed and approved
- Date/time

Use `/compliance:audit-export` to assemble an exportable pack. Skills that produce file-bound drafts include an **AUDIT LOG** block listing those fields (values `TBD` if unknown — never invent an approver).

---

## 8. Privacy and data handling

- Prefer Australian hosting / APP-compliant contractual commitments recorded in the org profile.
- Default against sending client PII to unapproved endpoints.
- Support the December 2026 automated-decision-making transparency obligation (APP 1.7) — if a skill's output could feed an automated decision with significant effect, flag it for the privacy policy owner.
- Client transcripts and fact-finds are sensitive; do not echo them into `~~chat` unless the user explicitly directs and the destination is inside the confidentiality perimeter.

---

## 9. Escalation paths

Route to the human / compliance owner rather than resolving:

- Complex or vulnerable clients
- Complaints and potential reportable situations (breach-triage)
- Incomplete information that would make personal advice or credit assistance unsafe
- Conflicts the licensee policy requires to be escalated
- Tax issues beyond a qualified tax relevant provider's confirmed scope (TPB)

---

## Condensed inline block (for skills)

Skills that produce consequential output should include this block in their Trust spine section:

```
DISCLAIMER: Standing "draft for licensed human review" stamp on every output.
SOURCING: Tag every product fact, lender-policy claim, rate, fee, and dollar
  amount as [sourced: <where>] or [verify] / [unverified — from training data].
ASSUMPTIONS: State load-bearing assumptions and incomplete-information warnings
  at the top — flag, don't fix.
NUMBERS: Never invent an input — flag INPUT NEEDED instead.
CONFIDENCE: Label output defensible draft vs structured first pass.
GATE: Before a file-ready / client-facing / lodgement version, confirm
  explicitly and stamp a reviewer note. The licensed human signs; this tool does not.
PROHIBITED: Do not select a product/lender as a client recommendation; do not
  finalise SOA/CAR/credit rationale; do not coach TMD gating questions.
```

Full rules: `../../references/trust-conventions.md`.

---

## Quick self-check

1. Is the **standing disclaimer** present?
2. Does **every material number or product/policy claim** have `[sourced: …]` or `[verify]`?
3. Are **load-bearing assumptions** and **incomplete-information** warnings at the top?
4. Is anything **invented** that should be `INPUT NEEDED`?
5. Is the **confidence label** honest — and does the output refuse to call itself advice?
6. For a **file-ready / client-facing** version, was confirmation obtained and a **reviewer note** stamped?
7. Would a file reviewer find the **BID / s961B (or NCCP Part 3-5A) scaffolding** they need, or only a polished narrative?
