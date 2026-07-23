---
type: phase-0-evidence-stub
gate: G9
status: OPEN
---

# G9 — Exception & Quality Edit Workflow Rules

**Status:** ⬜ OPEN

## Rules

1. Quality / reasonableness / policy exception → `man_review_status = true`  
2. Record **locked** until `reviewer_id` + `review_timestamp` + `review_rationale`  
3. Cannot **file** ReportPackage with open critical flags  
4. No silent discard of anomalous rows  

## Workflow log (template)

| Date | Record/uid | Flag reason | Reviewer | Decision | Rationale |
|------|------------|-------------|----------|----------|-----------|
| | | | | confirm / correct / escalate | |
