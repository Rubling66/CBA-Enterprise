---
type: system-architecture
product: CBA-Enterprise
status: pre-construction
date: 2026-07-23
agent: engineer-grok
---

# System Architecture — CBA-Enterprise

**No code.** Context, flows, boundaries, multi-tenant rules.

---

## 1. Context (C4 L1)

```
┌─────────────┐     feed / SFTP / API      ┌──────────────────────┐
│ Bank core   │ ─────────────────────────► │ CBA-Enterprise       │
│ (JH/Fiserv/ │                            │  ingest → track →    │
│  FIS / file)│ ◄─── reports / export ───  │  report → verify     │
└─────────────┘                            │  (+ gate optional)   │
                                           └──────────┬───────────┘
┌─────────────┐   public / licensed APIs              │
│ Municipal / │ ──────────────────────────────────────┤
│ open data   │                                       │
└─────────────┘                                       ▼
┌─────────────┐                            ┌──────────────────────┐
│ Examiners / │ ◄── package via bank ───── │ Bank compliance user │
│ OCC review  │                            │ + auditor_ro         │
└─────────────┘                            └──────────────────────┘
```

**Out of system:** Hermes agents, public ChatGPT, DHP consumer packs as *runtime dependencies*.  
**Allowed later:** DHP/city outcomes as **Verify sources** (fourth party), not bank data plane.

---

## 2. Logical modules (engine/)

| Module | Path (scaffold) | Responsibility |
|--------|-----------------|----------------|
| **Ingest** | `engine/src/ingest` | Consent orders / CBA PDFs / structured obligation import |
| **Track** | `engine/src/track` | Disbursement events → category, geography, commitment link |
| **Report** | `engine/src/report` | OCC-format packages, quarterly statements, immutable snapshots |
| **Verify** | `engine/src/verify` | Triple-blind: bank × municipal × anomaly flags |
| **Gate** | `engine/src/gate` | Consumer eligibility: identity → income/LMI → credit floor → lien → program match |

**Dashboard** (`dashboard/`): presentation only; **no business truth** without engine APIs.

---

## 3. Primary data flow

```
1. INGEST
   ConsentOrder / CBA contract → Commitment rows ($, category caps, deadlines, cites)
2. TRACK
   Bank disbursement batch → validate → Disbursement events (idempotent) → rollups
3. REPORT
   Period close → ReportPackage (versioned, hashed) → bank download / auditor view
4. VERIFY (async / period)
   For sample or full set: join public evidence → VerificationResult + human review flag
5. GATE (separate product surface)
   Consumer application → EligibilityDecision (not mixed into bank report tables)
```

### Integration surface (v1 vs later)

| Source | v1 | Later |
|--------|----|-------|
| Bank file drop (CSV/SFTP) + checksum | **Yes** | Real-time core APIs |
| Jack Henry / Fiserv / FIS | Design hooks only | Per-bank integration project |
| HMDA platform | Taxonomy lessons; not full HMDA submitter | Optional crosswalk |
| Municipal open data (Detroit first) | Manual/API pull for Verify | Automated refresh jobs |

---

## 4. Multi-tenant isolation

| Rule | Implementation intent |
|------|------------------------|
| Tenant = one **Institution** | All rows carry `institution_id` |
| No cross-tenant queries | App-layer filter + DB RLS when implemented |
| Keys & secrets | Per-tenant credentials for feeds |
| Operators | Vendor ops can support but every action audited |
| Reports | Cannot mix institutions in one package |

---

## 5. Triple-blind verification pipeline

```
        ┌──────────────┐
        │ Bank facts   │  (disbursement as reported)
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ City / public│  (license, permit, property, program records)
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │ Anomaly layer│  (duplicates, impossible geos, statistical outliers)
        └──────┬───────┘
               │
               ▼
     VerificationResult { status, evidence[], needs_human_review }
```

**Black-box rule:** Anomaly flags never auto-“prove impact” without human-reviewable evidence chain.

---

## 6. Consumer eligibility gate (architecture only)

```
Identity proof → Income / LMI screen → Credit floor policy → Lien / title screen
    → Program match (against Commitment categories) → EligibilityDecision
```

- **Separate schema namespace** from bank reporting tables.
- Highest privacy heat → last construction phase.
- Outputs may later feed **Verify** (outcome occurred), not bank core.

---

## 7. Security & ops boundaries

| Concern | Decision |
|---------|----------|
| Auth | Bank IdP/SSO preferred; MFA required for vendor ops |
| Secrets | Env/secret manager; never in git |
| AI | Local only on non-confidential or redacted text |
| Environments | dev / stage / prod |
| Change control | Prod promote only with logged approval |

---

## 8. Phase construction (stress before next)

| Phase | Build | Stress before next |
|-------|-------|--------------------|
| 0 | Policies + isolation rules | Due-diligence packet completeness |
| 1 | Ingest + Report | Bad PDFs, wrong $, re-file immutability |
| 2 | Track | Duplicate feeds, late restatements, category remap after file |
| 3 | Verify | Missing city data, false positive rate review |
| 4 | Gate | PII abuse, retention wipe, role escalation |

---

## 9. Explicit non-goals (anti-drift)

- Not a general CRM  
- Not a core banking replacement  
- Not bulk consumer marketing engine  
- Not DHP prompt library  
- Not lots313 geometry  
