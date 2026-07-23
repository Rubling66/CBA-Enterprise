---
type: data-plane-spec
product: CBA-Enterprise
status: PRE-CONSTRUCTION — backside only
date: 2026-07-23
agent: engineer-grok
source: Commander research Q3 part 2 (HMDA/CRA/1071 + SOC 2 Type II patterns)
---

# Data Plane Specification (Backside Only)

**No UI.** Ingestion and ledger behavior enforce integrity **independent of frontend validation** (frontend may help operators; backend is law).

Aligns with: Phase-0 **G1, G2, G8, G9, G10** and `docs/architecture/data-model.md`.

CBA-Enterprise is **not** a full HMDA LAR filing product, but **field discipline, edit checks, immutability, and human-in-the-loop** follow federal reporting patterns so bank examiners recognize the control language.

---

## (a) Field-level contract sketch

Ingestion expects strict schema adherence (CSV or pipe-delimited text, **UTF-8**, no decorative leading-zero padding beyond schema rules).

| Field | Type / rule | Notes |
|-------|-------------|--------|
| `uid` | String 21–45 chars | Begins with institution **LEI**; **no consumer PII**; globally unique |
| `app_date` | Date | Real calendar date; strictly `YYYYMMDD` |
| `action_taken_date` | Date | `YYYYMMDD`; see chronological invariant |
| `action_taken` | Integer enum (e.g. 1–5) | e.g. 1=Originated, 3=Denied — pin codebook version |
| `loan_amount` | Float/Decimal | Must be **> 0** (or explicit NA code if schema allows); catch missing-decimal outliers |
| `denial_reasons` | Integer array | If `action_taken`=Denied, required valid codes; if “Other” (e.g. 977), free-form **not blank** (max 300 chars) |
| `gross_annual_revenue` | Float | If known, not blank; no revenue → explicit **0** (not null) |
| `man_review_status` | Boolean | Default `false`; quality/anomaly → `true` and **lock** until review metadata present |
| `reviewer_id` | String | Required when `man_review_status`=true to unlock |
| `review_timestamp` | ISO datetime | Required with reviewer |
| `review_rationale` | String | Required with reviewer (exception / confirm / correct) |

**CBA mapping:** Map HMDA/1071-style fields onto `Disbursement` / obligation lines where applicable; maintain **codebook version** in lineage matrix (G1/G8).

**Idempotency:** Prefer `uid` (or bank `idempotency_key`) as register-level unique key — see stress matrix.

---

## (b) Integrity invariants

1. **Syntactical invariance** — Types and structural limits absolute (e.g. Census Tract GEOID **exactly 11 digits**; `uid` alphanumeric only per rule).  
2. **Chronological invariance** — `action_taken_date` ≥ `app_date`.  
3. **Conditional independence** — If Denied/Withdrawn, conditional pricing fields must be explicit **NA code** (e.g. 999), never ghost values.  
4. **Multi-value restriction** — Mutually exclusive states cannot co-exist (e.g. entity applicant + human credit score).  
5. **Filed immutability** — Finalized report period packages are locked; corrections → **new version** + resubmission workflow (not in-place rewrite).  
6. **Human-in-the-loop** — Quality-edit / reasonableness flags cannot clear without reviewer_id + timestamp + rationale (G9).  
7. **Tenant isolation** — Every row carries `institution_id`; no cross-tenant register writes.  
8. **LLM boundary** — Restricted classes never leave controlled plane to public models (G10).

---

## (c) Stress matrix (expected system behavior)

| Stress scenario | Trigger | Expected behavior | Result |
|-----------------|---------|-------------------|--------|
| **Duplicate payments / records** | Payload `uid` already in reporting dataset | **FAIL FAST.** Reject at register (e.g. Error E3000: `uid.duplicates_in_dataset`). No double-count commit | **PASS** if rejected |
| **Missing categories** | Required demographic/financial field null without NA/Exempt code | **HALT & FLAG.** Syntactical/validity edit; dead-letter / quarantine for remediation | **PASS** if halted |
| **Late restatements** | Q2 txn modified in Q4 after period report **locked** | **VERSION & ALERT.** Original immutable; new version; Resubmission workflow; officer cert before regulator delta | **PASS** if versioned |
| **Category reclass after filed** | Tract/product updated after locked artifact | **QUALITY EDIT LOCK.** Divergence flagged; `man_review_status`=true; no silent overwrite of filed package | **PASS** if locked+flagged |
| **Feed outage mid-quarter** | Core API drop (e.g. 14h) | **QUEUE & RECONCILE.** Secure queue; on reconnect, freshness/SLA sentinel runs gap ingest | **PASS** if gap recovered |
| **Auditor read-only abuse** | Auditor bulk-exports unmasked PII via script | **BLOCK & LOG.** Rate limit + RBAC; SIEM anomalous volume; session terminate; alert incident commander | **PASS** if blocked |

---

## Backend-only enforcement rule

| Layer | Role |
|-------|------|
| API / gateway | AuthZ, rate limit, tenant header |
| Ingest service | Schema + syntactical + validity edits |
| Register / DB | Unique constraints, immutability on filed snapshots |
| Workflow | G9 manual review lock |
| SIEM | G6 alerts on abuse / missing logs |
| Frontend | Operator convenience only — **never sole control** |

---

## Link to modules

| Module | Data-plane duty |
|--------|-----------------|
| M1 Ingest | Schema + lineage + fail-fast duplicates |
| M2 Track | Idempotent events; quarantine missing categories |
| M3 Report | Lock filed packages; resubmission versions |
| M4 Verify | Quality edits → G9 queue; never auto-prove |
| M5 Gate | PII class; G10 hard boundary |

---

## Evidence artifacts to fill

| Artifact | Gate |
|----------|------|
| `docs/compliance/artifacts/EXCEPTION_AND_QUALITY_EDIT_WORKFLOW.md` | G9 |
| `docs/compliance/artifacts/DATA_CLASSIFICATION_AND_AI_GUARDRAILS_MATRIX.md` | G10 |
| `docs/compliance/artifacts/REGULATORY_EDIT_CHECKS_AND_MOCK_SUBMISSION.md` | G8 |
| `docs/compliance/artifacts/DATA_LINEAGE_MAPPING_MATRIX.md` | G1 |
