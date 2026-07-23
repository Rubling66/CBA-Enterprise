---
type: market-intelligence
product: CBA-Enterprise
status: research-absorbed
date: 2026-07-23
agent: engineer-grok
source: Commander competitive research (Detroit CBA/CRA/CDFI ecosystem)
---

# Detroit CBA / CRA Competitive Landscape

**Use:** Positioning for bank vendor sale of **CBA-Enterprise** (disbursement tracking + OCC-ready reporting + prove layer).  
**Not:** A claim that we compete as a bank or CDFI lender.

---

## 1. Market definition

Detroit’s CBA/CRA field is shaped by:

1. **Large, bank-specific capital pledges** (often NCRC-brokered nationally, with Detroit flagship carve-outs)  
2. **Dense CDFI intermediary network** — banks rarely deploy CBA capital alone  
3. A **persistent gap** in **micro-lending &lt;$100k** to LMI and majority-minority tracts despite headline billions  

**Product wedge:** Banks can **pledge** and **route** capital; they still struggle to **prove to examiners and communities** where dollars landed, by category and geography — especially for small business micro-credit. That is the reporting/prove gap CBA-Enterprise fills.

---

## 2. Key bank competitors & Detroit-specific investments

Major institutions use Detroit as a **flagship proof market** for national CBA/CRA strategy.

| Institution | Detroit / related commitment (research) | Notes for vendor positioning |
|-------------|----------------------------------------|------------------------------|
| **JPMorgan Chase** | ~$200M holistic Detroit recovery investment; $17M Strategic Neighborhood Fund (SNF); $15M Detroit Housing for the Future Fund (DHFF); **Entrepreneurs of Color Fund (EOCF)** with Kellogg + Detroit Development Fund | Strong CDFI + neighborhood fund stack; EOCF = minority business capital narrative |
| **Huntington** | Post-TCF: **$40B** national Community Plan; **$1B** exclusive Detroit/Wayne County; $10M SNF; Pure Michigan Micro Lending ($25M state partnership) | Explicit Detroit carve-out; micro-lending already in brand story — needs **proof** of reach |
| **Comerica** | Hometown; **Outstanding** CRA PE (2025 Fed research cite); $1.8B mortgages + $2.8B small business in AAs over eval period; historical **$4.2B** CBA with Detroit Alliance for Fair Banking | High CRA bar; reporting vendor must match examiner-grade rigor |
| **Fifth Third** | NCRC CBA: **$41.6B** vs $32B goal; Detroit **$5M Gratiot/7 Mile (G7)** neighborhood model; EOCF investment | Hyper-local neighborhood adoption → **tract-level** reporting is the sales language |

**Also in product target list (architecture docs):** Flagstar (~$2B class commitments in internal target table).

---

## 3. CDFI / intermediary ecosystem (not competitors — channel)

Banks **route** capital through intermediaries to reduce risk and reach underserved borrowers.

| Entity | Role | Implication for CBA-Enterprise |
|--------|------|--------------------------------|
| **Detroit CDFI Coalition** (~19+ institutions) | Collective capital direction; “CDFI Grid” for navigation | **Prove** layer may need CDFI/org as counterparty type + referral path metadata |
| **Invest Detroit / SNF** | SNF ~$75M philanthropic + ~$110M public leverage; &gt;70% projects led by developers of color / local orgs | Housing/community_development categories; outcome evidence via project/org |
| **Capital Impact Partners / EDI** | Equitable Development Initiative (w/ JPMC support) — developers of color | Workforce + community development pathways |
| **Detroit Development Fund** | EOCF partner; micro/minority business capital | Primary **referral pipeline** partner for micro-gap narrative |

**Product rule:** Model **disbursement counterparties** as bank | CDFI | nonprofit | household | other — not bank-only.

---

## 4. Market gap: micro-lending disparities

Source pattern: *Patterns of Disparity*–style small business lending analysis (research summary):

| Segment | Share of businesses (region) | Share of CRA-reported bank loans **&lt;$100k** |
|---------|------------------------------|-----------------------------------------------|
| Low-income Detroit census tracts | ~10% | **~5%** |
| Majority-minority census tracts | ~10.1% | **~6.2%** |

**Strategic takeaway**

- Banks **have** deployed large capital into **real estate and neighborhood funds** (SNF, G7, DHFF).  
- Market still **underserves LMI and minority entrepreneurs** needing **micro-loans &lt;$100k**.  
- Winning bank **strategy** (and our **reporting product**): move beyond broad goals → **hyper-target** micro-lending to specific tracts, with **CDFI referral pipelines** and **tract-level proof**.

---

## 5. What this means for CBA-Enterprise (product)

| Capability | Competitive use |
|------------|-----------------|
| **Category taxonomy** | `small_business` must support **micro** tier (&lt;$100k) as first-class slice, not only large commercial |
| **Geography** | Tract/MSA rollups required for disparity narrative and CRA-adjacent exam talk |
| **Track** | Disbursement size bands + counterparty type (incl. CDFI) |
| **Report** | Commitment vs disbursed by category **and** micro band; deadline package for OCC/CBA |
| **Verify (M4)** | Link small biz loans to public signals where possible; flag gaps in LMI/majority-minority tracts |
| **Not in scope** | Becoming a lender or replacing CDFIs |

**Sales line (honest):**  
*You already pledged Detroit. We help you show examiners and the city — by category, tract, and micro-loan band — where the money went, including through CDFI partners.*

---

## 6. Competitive set for *our* product (software/vendor)

This research describes **capital competitors** (banks). Software competitors still TBD (internal research tag: competitor software). Placeholder:

| Type | Examples to research | Differentiator |
|------|----------------------|----------------|
| Generic GRC / compliance suites | Enterprise GRC tools | Not Detroit CBA/CDFI-native |
| CRA reporting tools | Legacy LAR/CRA shops | We focus **CBA consent-order + disbursement prove** |
| Homegrown bank Excel | Still common | Immutability + audit trail + multi-tenant |

---

## 7. Target bank priority (Detroit-first, from this intel)

| Priority | Bank | Hook |
|----------|------|------|
| 1 | Huntington | $1B Detroit/Wayne + micro-lending story |
| 2 | JPMC | Flagship Detroit + EOCF/CDFI complexity |
| 3 | Comerica | Outstanding CRA + hometown scrutiny |
| 4 | Fifth Third | G7 hyper-local → tract proof |
| 5 | Flagstar | Regional footprint (prior target list) |

---

## 8. Open research (do not invent)

- [ ] Pin primary sources + dates for all $ figures (NCRC agreements, CRA PEs, SNF reports)  
- [ ] Software competitor matrix  
- [ ] CDFI Grid fields worth modeling as reference data  
- [ ] Exact *Patterns of Disparity* citation for exam-facing deck  

---

## 9. Cross-links

- Product skeleton: `README.md`  
- Categories/geo: `docs/architecture/data-model.md`  
- Phase-0: `docs/compliance/PHASE-0_ACCEPTANCE_CHECKLIST.md`  
- Targets also in: `docs/architecture/system-architecture.md`  
