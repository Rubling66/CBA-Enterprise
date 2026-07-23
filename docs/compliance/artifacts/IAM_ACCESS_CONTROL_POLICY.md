---
type: phase-0-evidence-stub
gate: G5
status: OPEN
---

# G5 — IAM Configuration & Access Control Policy

**Status:** ⬜ OPEN

## Roles

| Role | Scope | MFA | Notes |
|------|-------|-----|-------|
| bank_admin | Own institution | Required | |
| bank_analyst | Own institution read/report | Required | |
| auditor_ro | Time-boxed read | Required | No edit |
| vendor_operator | Support under audit | Required | JIT privilege |

## Controls

- [ ] RBAC + least privilege  
- [ ] MFA on prod, cloud consoles, dashboards  
- [ ] Quarterly access review  
- [ ] No standing god-admin; JIT for privilege  
- [ ] Tenant isolation (`institution_id`)  
