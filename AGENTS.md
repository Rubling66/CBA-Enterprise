# AGENTS.md — CBA-Enterprise (binding for Grok / Hermes builders)

**Repo:** https://github.com/Rubling66/CBA-Enterprise  
**Local:** `C:\Users\Admin\CBA-Enterprise`  
**Status:** Pre-construction — Phase-0 framework. **No feature code until Phase-0 scoreboard policy is green.**

---

## Mission

Bank **Community Benefits Agreement (CBA)** / consent-order **compliance reporting** vendor product.  
Revenue pin: ~$2,500/yr per institution. Detroit banks first.

**You build the product. The product enforces compliance. Bank PII never enters a public LLM (including this agent on restricted data).**

---

## Two planes (do not merge)

| Plane | Purpose | This agent may |
|-------|---------|----------------|
| **Build plane** | Code, docs, CI on **synthetic / public / redacted** | Yes |
| **Runtime plane** | Live bank data, LAR-style registers, SARs | **No** — never paste or load real bank/customer files here |

See: `docs/architecture/BUILD_PLANE_VS_RUNTIME_PLANE.md`

---

## Phase-0 freeze law

Canonical: `docs/compliance/PHASE-0_ACCEPTANCE_CHECKLIST.md` (G1–G10)

| Before… | Require |
|---------|---------|
| Ingest real bank feeds | G1, G2, G9, G10 + scoreboard |
| External API / cloud / model on data path | G4, G5, G6, G10 |
| AI/ML on credit/eligibility | G7 or signed N/A-no-AI |
| Regulator-grade field export | G8 |
| Prod deploy with financial data | G3 (2-person), G5 MFA |

**Default v1:** No AI on bank exam path → prefer **N/A — no AI** until Commander opens G7.

---

## G10 — NEVER paste / process in this agent

- PII: SSN, PAN, accounts, biometrics, unredacted credit, exact KYC/AML  
- Secrets: API keys, `.env`, SSH, DB passwords  
- BSA/SAR, internal risk/vuln reports, exam confidential  
- Live bank disbursement files with customer identifiers  
- Proprietary infra configs with real URLs/keys  

**Allowed:** synthetic samples under `data/samples/`, public OCC/FFIEC text, redacted architecture.

Playbook: `docs/compliance/artifacts/DATA_CLASSIFICATION_AND_AI_GUARDRAILS_MATRIX.md`  
Data plane: `docs/compliance/DATA_PLANE_SPEC.md`

---

## Module order (when construction opens)

1. M1 Ingest + M3 Report  
2. M2 Track  
3. M4 Verify  
4. M5 Gate (last — PII heat)

Scaffold only under `engine/src/{ingest,track,report,verify,gate}/` until BUILD-ORDER.

---

## Bridge protocol (Hermes ↔ Grok)

| Path | Direction |
|------|-----------|
| `D-Obsidian/Bridge/to-grok/` | Hermes → Grok (tasks) |
| `D-Obsidian/Bridge/from-grok/` | Grok → Hermes (status) |
| `D-Obsidian/Bridge/PROTOCOL.md` | Naming + priorities |

On task complete: write `from-grok/YYYY-MM-DD_HHMM_P*_TYPE_SUBJECT.md` and **commit + push**.

---

## Git / commit rules

- Commit docs and framework to `origin/master` when work lands  
- Never commit `.env`, keys, real customer CSV/JSON  
- Prefer complete sentences in commit messages  
- No force-push to master  

---

## Anti-drift

Do **not** architect into this repo: DHP prompt packs, lots313 geometry, Hermes runtime as bank data plane, public LLM as compliance decision engine.

**Stack truth:** Deterministic edit/register logic in **our code**. Grok Build = **build tool**, not bank runtime.
