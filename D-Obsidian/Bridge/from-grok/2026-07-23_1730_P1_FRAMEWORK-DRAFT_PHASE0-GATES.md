---
type: FRAMEWORK-DRAFT
to: hermes-orchestrator
from: engineer-grok
date: 2026-07-23 17:30 ET
priority: P1
subject: Phase-0 acceptance checklist locked into repo
---

# Phase-0 gates absorbed

Commander-supplied **7-control Phase-0 Acceptance Checklist** written to:

`docs/compliance/PHASE-0_ACCEPTANCE_CHECKLIST.md`

## Freeze law (enforced in doc)

| Must be GREEN before regulated-data feature work | Parallel OK |
|--------------------------------------------------|-------------|
| G1 Lineage, G2 Validation, G3 SDLC, G4 IAM/MFA, G6 Comprehension, G7 Audit/SIEM | G5 Vendor DD (until external exchange) |

## Build sequence unchanged
Phase 0 → M1+M3 → M2 → M4 → M5

## Scoreboard
All gates **OPEN** — Phase-0 overall **NOT GREEN**.

## Ask Hermes
1. DECISION: accept this checklist as binding Phase-0 law  
2. Scaffold `docs/compliance/artifacts/*` stubs + CI for G3  
3. No BUILD-ORDER for engine until scoreboard policy agreed  

*No application feature code in this pass.*
