# Bridge Protocol — CBA-Enterprise

## Channels

```
D-Obsidian/Bridge/
├── to-grok/       # Hermes writes → Grok reads (task briefs, architectures, decisions)
├── from-grok/     # Grok writes → Hermes reads (status, evidence, blockers)
└── shared/        # Reference files both sides read (architecture docs, regs)
```

## File Naming Convention

```
YYYY-MM-DD_HHMM_DIRECTION_SUBJECT.md
```

Examples:
- `2026-07-23_1545_to-grok_FRAMEWORK-REQUEST.md`
- `2026-07-23_1800_from-grok_ARCHITECTURE-DRAFT.md`
- `2026-07-24_0600_from-grok_OVERNIGHT-STATUS.md`

## Priority Tags

| Tag | Meaning | Response Window |
|-----|---------|----------------|
| P0 | Executing now — no questions | Immediate |
| P1 | Within 4 hours | Same session |
| P2 | End of day | EOD |
| P3 | By next session | 24h |

## Hermes → Grok Message Types

1. **FRAMEWORK-REQUEST** — "Architect this — no code yet"
2. **BUILD-ORDER** — "Build this module — spec attached"
3. **DECISION** — "We chose X — adjust trajectory"
4. **RESEARCH** — "Find/verify this — return evidence"

## Grok → Hermes Message Types

1. **FRAMEWORK-DRAFT** — Architecture proposal with rationale
2. **BUILD-EVIDENCE** — What was built, commit SHA, test results
3. **BLOCKER** — Something needs Commander/Hermes decision
4. **STATUS** — Session close, what's done, what's next

## Startup Sequence

1. Hermes: write `to-grok/FRAMEWORK-REQUEST.md`
2. Grok: acknowledge, load architecture, return `from-grok/FRAMEWORK-DRAFT.md`
3. Hermes: review, write `to-grok/DECISION.md` with adjustments
4. Grok: implement, return `from-grok/BUILD-EVIDENCE.md`

## Example Flow

```
Hermes → to-grok/2026-07-23_1545_P0_FRAMEWORK-REQUEST_CBA-DATA-MODEL.md
Grok   → from-grok/2026-07-23_1800_P1_FRAMEWORK-DRAFT_CBA-DATA-MODEL.md
Hermes → to-grok/2026-07-23_1830_P0_DECISION_CBA-DATA-MODEL-APPROVED.md
Grok   → from-grok/2026-07-24_0200_P1_BUILD-EVIDENCE_CBA-INGEST-ENGINE.md
```

## Reference Files (shared/)

Copied from `docs/` when Grok needs them:
- `docs/regulatory/OCC-2013-29-vendor-management.md`
- `docs/architecture/system-architecture.md`
- `docs/compliance/SOC2-readiness-plan.md`
