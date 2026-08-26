# SOA / ROA / Client Advice Record — content scaffolding

**Not legal advice. Verify current law before relying on this file.** DBFO Tranche 2 proposed replacing the Statement of Advice with a simpler Client Advice Record (CAR). That change was **not settled law** at design time. The `soa-draft` skill is **mode-switchable**: current SOA (default) or CAR (only when the licensee confirms the CAR regime applies to this file).

## Current SOA content (ss947B / 947C / 947D) and RG 175

RG 175 (updated November 2024) requires advice documents to be **clear, concise and effective**. Scaffold drafts around these elements the **adviser completes**:

| Element | Notes for the draft |
|---|---|
| Advising entity and authorising licensee | From org / practice profile; never invent licence numbers |
| Client identity and advice date | From fact-find; `INPUT NEEDED` if missing |
| Statement of advice vs further advice (ROA) | User selects mode; ROA is further advice, not a first SOA |
| Client's relevant circumstances | Objectives, financial situation, needs — from fact-find |
| Scope of advice | In-scope / out-of-scope; do not silently widen |
| Recommended strategy and products | **Adviser authors.** Model may structure headings and pull APL facts with `[sourced:]` / `[verify]`. Never select the product. |
| Information about each recommended product | From APL / PDS / TMD the user supplied |
| Reasons why the advice is appropriate / in best interests | Adviser authors; model offers a prompt list, not the conclusion |
| Alternative strategies / products considered | Structure only; adviser fills |
| Costs, fees, commissions, conflicts | From licensee fee schedule / product docs; never invent |
| Replacement-of-product disclosure (s947D) where relevant | Flag if a replacement is in scope; do not skip |
| Authorising signature block | Blank for the relevant provider |

## ROA (Record of Advice / further advice)

Use when the client already has an SOA and circumstances have not changed in a way that requires a new SOA, **as the adviser determines**. The draft is shorter: what changed, what is recommended, why, costs. If circumstances look materially different, flag `[review]` — new SOA may be required; the adviser decides.

## Client Advice Record (CAR) mode

Only when the practice profile or the user states the CAR regime applies:

- Prefer the licensee's CAR template over this scaffold
- Keep BID scaffolding (`bid-s961b.md`) — CAR does not, by itself, remove s961B/s961G/s961J
- Still require the human to author the recommendation and reasoning
- Stamp `MODE: CAR [licensee-confirmed]` at the top so a file reviewer can see which regime the draft assumed

If the user has not confirmed CAR applies, **default to SOA** and say so.

## Clear, concise and effective

- Short sentences; defined terms; no filler
- Recommendation and reasoning in the adviser's voice after they supply it — not the model's
- Appendices for product details rather than burying the client's "so what"
