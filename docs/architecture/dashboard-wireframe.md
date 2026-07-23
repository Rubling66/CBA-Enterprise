---
type: dashboard-wireframe
product: CBA-Enterprise
status: pre-construction
date: 2026-07-23
agent: engineer-grok
---

# Dashboard Wireframe — CBA-Enterprise

**No code / no pixels.** Information architecture for three audiences.  
**Rule:** UI never invents numbers — only engine APIs / filed packages.

---

## 1. Global chrome

| Element | Behavior |
|---------|----------|
| Institution switcher | Bank_admin multi-org only; single-tenant users fixed |
| Period selector | Quarter / year aligned to Commitment cadence |
| Environment badge | PROD / STAGE clearly marked |
| Role badge | bank_admin / bank_analyst / auditor_ro / vendor_ops |
| “As of” timestamp | Last successful Track ingest |

---

## 2. Bank view (primary revenue UI)

### 2.1 Home — Exam readiness
| Panel | Content |
|-------|---------|
| Commitment vs disbursed | $ and % by category |
| Deadline strip | Next OCC/CBA reporting deadlines from Ingest |
| Exam readiness score | Checklist: data freshness, open exceptions, filed package present |
| Exceptions queue | Failed rows, unmapped categories, Verify flags needing human |

### 2.2 Commitments
- Table: category, committed, disbursed, remaining, period, status  
- Drill → disbursement list for that commitment  

### 2.3 Disbursements
- Filters: category, geo, date, batch  
- Row → external_ref, amount, geo, verify status  
- Export CSV (audited)  

### 2.4 Geography
- Heatmap / ranked tracts or ZIPs (aggregate)  
- No parcel dump on default bank home  

### 2.5 Reports
- List ReportPackages: period, version, status (draft/filed/superseded), hash  
- Actions: generate draft, preview, **file** (permissioned), download, supersede  
- Filed = download only + audit  

### 2.6 Verify
- Queue: needs_human_review  
- Evidence side-by-side: bank fact vs city cite  
- Decision: accept / reject / escalate (AuditEvent)  

### 2.7 Admin
- Users/roles, feed credentials status, subprocessor page (read-only for bank)  

---

## 3. Consumer view (Gate — phase last)

| Screen | Content |
|--------|---------|
| Start | Purpose notice + consent |
| Status | EligibilityDecision + reason codes |
| Programs | Matched program list (from commitments) |
| Tracker | Application steps (if intake exists) |
| Privacy | Retention / delete request entry |

**Not on consumer home:** bank internal commitments $, examiner tools, other consumers.

---

## 4. Regulator / auditor view

| Screen | Content |
|--------|---------|
| Package library | Filed packages only |
| OCC-format export | One-click download of filed snapshot |
| Audit log | Filter by actor/entity/time |
| Verification evidence | Read-only chain for sampled lines |
| No edit | No draft generation; no category remap |

Access: time-boxed `auditor_ro` grant per institution.

---

## 5. Navigation map

```
Bank:
  Home → Commitments → Disbursements → Geography → Reports → Verify → Admin

Consumer:
  Home → Status → Programs → Privacy

Auditor:
  Packages → Audit log → Evidence
```

---

## 6. Empty / error / stress UI states

| State | UI |
|-------|-----|
| No ingest yet | “Connect first file” + period empty |
| Stale feed | Banner: last ingest age > threshold |
| Filing blocked | List failed phase-0/data checks |
| Supersede | Warn: prior filed version remains |
| Cross-tenant | Hard deny page |

---

## 7. Anti-slop / anti-drift

- No vanity charts without engine backing  
- No “AI insights” panel in v1 bank exam path  
- No mixing consumer Gate chrome into bank exam home  
