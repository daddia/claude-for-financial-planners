# AI-use governance — ASIC REP 798 module

**Not legal advice.** ASIC REP 798 "Beware the gap" (29 October 2024, 24-238MR) reviewed 624 AI use cases across 23 AFS and credit licensees. Existing obligations apply to AI-assisted work (technology-neutral): Best Interests Duty, efficiently/honestly/fairly, misleading conduct, directors' duties, record-keeping.

This module turns ASIC's **11 governance questions** into setup steps for `/compliance:ai-governance-setup`. It does not certify that the licensee's arrangements are adequate.

## Eight key findings (for the inventory narrative)

1. Adoption varies but is accelerating
2. Shift toward more complex/opaque techniques; generative AI increasing
3. Deployment mostly cautious — AI augmenting rather than replacing human decisions
4. Not all licensees had adequate AI-risk arrangements
5. Some assessed risk through a business rather than consumer lens (algorithmic bias gaps)
6. Governance arrangements varied widely
7. Governance/risk maturity did not always match the nature and scale of AI use — greatest consumer-harm risk
8. Heavy reliance on third-party models without appropriate governance

## 11 questions → setup fields

| # | ASIC question (paraphrased) | Capture in the AI inventory |
|---|---|---|
| 1 | Taking stock / AI inventory | Every AI use case this practice uses or is developing, including this plugin |
| 2 | Strategy | Why AI is used; what it must never do (no autonomous personal advice / credit assistance) |
| 3 | Ethics & fairness | Australian AI Ethics Principles — note, don't tick-box certify |
| 4 | Accountability | Named human accountable for each AI-involved decision |
| 5 | Risk | Consumer-harm lens, not only business-process risk |
| 6 | Alignment of governance to use | Scale of use vs. oversight intensity |
| 7 | Policies | AI-use policy exists? If not, draft a template for compliance to finish |
| 8 | Resourcing | Who monitors outputs and model drift |
| 9 | Oversight & monitoring | Cadence; root-cause of unexpected outputs |
| 10 | Third parties | This plugin and any other vendor — same governance as internal tools |
| 11 | Engagement with reform | Owner who watches ASIC/Treasury/DBFO updates |

## Better practices to encode as defaults

- Board- or licensee-level reporting on holistic AI risk
- Documented **human-in-the-loop** accountable for each AI-involved decision
- Periodic drift / unexpected-output review
- Same governance for third-party models as for internal ones

## Since REP 798 — supervisory expectations have moved

**Verify all of this against the primary sources before relying on it.** REP 798 remains the anchor document and its 11 questions are still the right skeleton, but its underlying data is a snapshot of AI use cases **as at December 2023**. Two later regulator communications sharpen what an inventory should capture:

| Source | Date | What it adds to the inventory |
|---|---|---|
| APRA, letter to industry on artificial intelligence `[verify]` | 30 April 2026 | Findings from late-2025 engagement with larger institutions: AI governance maturity gaps, and **overreliance on vendor presentations and summaries without sufficient examination of key AI risks**. Board **AI literacy** and oversight of an AI strategy aligned to risk appetite are expressed as expectations. |
| ASIC, letter to industry (26-092MR) `[verify]` | 8 May 2026 | Cyber resilience against frontier AI models — "do not wait for perfect clarity to address the threat posed by new AI models." A back-to-basics posture on core cyber risk management rather than AI-specific controls. |

### What this changes in `/compliance:ai-governance-setup`

- **Question 10 (third parties) carries more weight than the others.** This marketplace *is* a third-party AI tool in the licensee's inventory. Record it as one, and record what the practice has actually examined about it — not what the vendor's README claims. A README is a vendor summary; APRA's finding is precisely about relying on those.
- **Question 3 (ethics) and question 4 (accountability) should capture board or principal AI literacy**, not just a named human per decision.
- **Question 11 (engagement with reform)** should name both regulators, not ASIC alone — APRA-regulated entities in the group pick up the APRA letter as well.
- Neither letter is a rule. Both are supervisory signals about what "adequate arrangements" is being read to mean. Do not present either as a compliance requirement in a draft — `[verify]` and route to the compliance owner.

### Seed sources for `regulatory-change-watcher`

When the watcher runs, these are the standing sources for the AI-governance thread: ASIC media releases and letters to industry, APRA letters to industry, Treasury DBFO consultations, and OAIC guidance on AI and the APP 1.7 automated-decision-making obligation commencing **10 December 2026**.

## Boundary this marketplace must keep

By remaining in "assist a licensed human" territory and never generating client-facing personal advice autonomously, the product stays clear of being a **digital advice provider** under RG 255. The inventory must record that boundary explicitly.
