---
type: data-model
product: CBA-Enterprise
status: pre-construction
date: 2026-07-23
agent: engineer-grok
---

# Data Model — CBA-Enterprise

**No code.** Entity contracts, taxonomy, integrity invariants, stress expectations.

---

## 1. Core entities

```
Institution 1──* ConsentOrder 1──* Commitment 1──* Disbursement
                     │                  │
                     │                  └──* Outcome (optional, via Verify)
                     │
                     └──* ReportPackage *──* ReportLine
Consumer (Gate only) 1──* EligibilityDecision
AuditEvent * (append-only, all tenants)
```

### Institution
| Field | Notes |
|-------|-------|
| id | UUID |
| legal_name | |
| chartering_id / RSSD optional | For bank identity |
| tenant_status | active / suspended / terminated |

### ConsentOrder
| Field | Notes |
|-------|-------|
| id | |
| institution_id | |
| regulator_cite | e.g. OCC order number |
| effective_date / end_date | |
| source_document_uri | Encrypted store pointer |
| raw_hash | Integrity of source file |

### Commitment
| Field | Notes |
|-------|-------|
| id | |
| consent_order_id | |
| category | Enum — see taxonomy |
| amount_committed | Decimal, USD |
| amount_disbursed_cached | Rollup (derived, rebuildable) |
| period_start / period_end | |
| geography_scope | MSA / county list / tract list |
| reporting_cadence | quarterly / annual |

### Disbursement
| Field | Notes |
|-------|-------|
| id | |
| commitment_id | |
| institution_id | Denormalized for RLS |
| event_time | |
| amount | |
| category | Must match or map to commitment |
| counterparty_type | business / household / nonprofit / other |
| geo | tract / county / MSA |
| external_ref | Bank’s payment/loan id |
| idempotency_key | **Required** — bank_id + external_ref + amount + date |
| source_batch_id | Feed batch |

### Outcome (Verify)
| Field | Notes |
|-------|-------|
| id | |
| disbursement_id | Optional link |
| evidence_source | municipal / license / permit / other |
| evidence_uri / cite | |
| status | matched / unmatched / inconclusive |
| needs_human_review | bool |
| method_version | Verification method pin |

### ReportPackage
| Field | Notes |
|-------|-------|
| id | |
| institution_id | |
| period | |
| version | Monotonic per period |
| status | draft / filed / superseded |
| content_hash | Manifest hash |
| filed_at / filed_by | Immutable once filed |
| storage_uri | Snapshot bytes |

### Consumer + EligibilityDecision (Gate)
| Field | Notes |
|-------|-------|
| consumer_id | Pseudonymous where possible |
| decision | eligible / ineligible / pending |
| reasons[] | Code list, not free prose only |
| program_matches[] | Commitment/category links |
| retention_until | |

### AuditEvent
| Field | Notes |
|-------|-------|
| id, ts, actor, action, entity_type, entity_id | |
| before_hash / after_hash | Optional |
| ip / session | Ops forensics |
| **Append-only** | Never update/delete in prod |

---

## 2. Category taxonomy

| Code | Label | Examples |
|------|-------|----------|
| `small_business` | Small business | Loans, grants, technical assistance $ |
| `homeownership` | Housing / homeownership | Purchase, rehab, down payment |
| `community_development` | Community development | Facilities, CDFI, neighborhood projects |
| `workforce` | Workforce | Training, apprenticeships, placement $ |

### Size band (Detroit micro-gap — market intel)

For `small_business` (and optionally all categories), track **amount band** for disparity reporting:

| Band | Definition | Why |
|------|------------|-----|
| `micro` | &lt; $100,000 | LMI / majority-minority tract gap per Detroit lending research |
| `standard` | ≥ $100,000 | Rest of commercial / larger credit |

**Counterparty type** (required for CDFI routing narrative): `bank` | `cdfi` | `nonprofit` | `household` | `other`.

**Invariant:** Every Disbursement.category ∈ taxonomy.  
**Mapping table:** Bank source codes → taxonomy (versioned); remap creates AuditEvent; **cannot change category on disbursements already in a filed ReportPackage** without superseding report.

**Market context:** `docs/market/DETROIT_CBA_CRA_COMPETITIVE_LANDSCAPE.md`

---

## 3. Geographic hierarchy

```
MSA → County → Census tract → Parcel (optional, high sensitivity)
```

| Level | Use |
|-------|-----|
| MSA / County | Default report rollups |
| Tract | LMI / CRA-adjacent analysis |
| Parcel | Gate / deep Verify only; restricted class |

---

## 4. Integrity invariants

1. **Tenant isolation:** every financial row has `institution_id`; queries always filtered.  
2. **Idempotent disbursements:** same idempotency_key → one row.  
3. **Committed ≥ 0; disbursed rollups rebuildable** from events.  
4. **Filed reports immutable:** status `filed` → bytes and hash frozen; corrections → new version + `superseded`.  
5. **Audit every promote:** draft → filed writes AuditEvent.  
6. **No silent delete** of Disbursement after include in filed package.  
7. **PII minimization:** Gate fields not copied into ReportLine by default.

---

## 5. Stress matrix (data plane)

| Scenario | Expected behavior |
|----------|-------------------|
| Duplicate payment file | Second load no double count (idempotency) |
| Missing category | Reject row or quarantine batch; no silent “other” |
| Late restatement after filed report | New package version; old remains for audit |
| Category reclass after filed | Block or supersede path only |
| Feed outage mid-quarter | Report shows as-of timestamp; incomplete flag |
| Cross-tenant ID guess | Zero rows / 403 |
| Auditor export | Read-only; full AuditEvent for export action |
| Anomaly false positive | needs_human_review=true; no auto-pass Verify |

---

## 6. What never enters public LLMs

- Raw consent-order PDFs with bank seals (unless synthetic)  
- Disbursement files with customer names/account numbers  
- Consumer SSNs / full credit payloads  
- Filed package contents for live banks  

Synthetic samples under `data/samples/` only for demos.

---

## 7. Schema delivery path (later construction)

When code opens: JSON Schema under `schemas/` matching these entities — still no feature code in this pass.
