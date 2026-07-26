"""
M3 Report — bank CBA compliance report (OCC-style narrative skeleton).

Uses synthetic fixtures until real bank feeds exist.
Output: JSON + Markdown under data/output/
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "engine" / "src"))

from ingest.load_commitment import load_commitment  # noqa: E402

OUT_DIR = ROOT / "data" / "output"


def _pct(disbursed: float, committed: float) -> float:
    if committed <= 0:
        return 0.0
    return round(100.0 * disbursed / committed, 2)


def build_report(data: dict[str, Any]) -> dict[str, Any]:
    commitments = data.get("commitments") or []
    disbursements = data.get("disbursements") or []
    by_cat: dict[str, dict[str, float]] = {}
    for c in commitments:
        cat = c["category"]
        by_cat.setdefault(cat, {"committed": 0.0, "disbursed_declared": 0.0, "disbursed_ledger": 0.0})
        by_cat[cat]["committed"] += float(c.get("committed_usd") or 0)
        by_cat[cat]["disbursed_declared"] += float(c.get("disbursed_usd") or 0)
    for d in disbursements:
        cat = d.get("category") or "other"
        by_cat.setdefault(cat, {"committed": 0.0, "disbursed_declared": 0.0, "disbursed_ledger": 0.0})
        by_cat[cat]["disbursed_ledger"] += float(d.get("amount_usd") or 0)

    micro_count = sum(1 for d in disbursements if d.get("size_band") == "micro")
    total_committed = sum(v["committed"] for v in by_cat.values())
    total_ledger = sum(v["disbursed_ledger"] for v in by_cat.values())

    rows = []
    for cat, v in sorted(by_cat.items()):
        rows.append(
            {
                "category": cat,
                "committed_usd": v["committed"],
                "disbursed_declared_usd": v["disbursed_declared"],
                "disbursed_ledger_usd": v["disbursed_ledger"],
                "pct_of_commitment_ledger": _pct(v["disbursed_ledger"], v["committed"]),
                "variance_declared_vs_ledger": round(
                    v["disbursed_declared"] - v["disbursed_ledger"], 2
                ),
            }
        )

    period = data.get("reporting_period") or {}
    report = {
        "report_type": "cba_compliance_period",
        "schema_version": "0.1.0",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "institution_id": data.get("institution_id"),
        "institution_name": data.get("institution_name"),
        "cba_id": data.get("cba_id"),
        "consent_order_ref": data.get("consent_order_ref"),
        "reporting_period": period,
        "summary": {
            "total_committed_usd": total_committed,
            "total_disbursed_ledger_usd": total_ledger,
            "overall_pct_disbursed": _pct(total_ledger, total_committed),
            "disbursement_count": len(disbursements),
            "micro_band_count": micro_count,
            "micro_band_share": round(100.0 * micro_count / max(len(disbursements), 1), 2),
        },
        "by_category": rows,
        "flags": [],
        "data_classification": "synthetic_fixture" if data.get("_meta", {}).get("synthetic") else "production",
        "ai_guardrail": "No consumer PII; tract GEOID optional aggregate only (G10)",
    }

    for row in rows:
        if abs(row["variance_declared_vs_ledger"]) > 1.0:
            report["flags"].append(
                {
                    "severity": "medium",
                    "code": "DECLARED_LEDGER_VARIANCE",
                    "category": row["category"],
                    "detail": f"variance ${row['variance_declared_vs_ledger']:,.2f}",
                }
            )
        if row["committed_usd"] > 0 and row["pct_of_commitment_ledger"] < 10:
            report["flags"].append(
                {
                    "severity": "low",
                    "code": "SLOW_DRAWDOWN",
                    "category": row["category"],
                    "detail": f"only {row['pct_of_commitment_ledger']}% of commitment in ledger",
                }
            )

    return report


def render_markdown(report: dict[str, Any]) -> str:
    s = report["summary"]
    lines = [
        f"# CBA Compliance Report — {report.get('institution_name')}",
        "",
        f"**CBA ID:** {report.get('cba_id')}  ",
        f"**Period:** {report.get('reporting_period')}  ",
        f"**Generated:** {report.get('generated_at')}  ",
        f"**Classification:** {report.get('data_classification')}",
        "",
        "## Summary",
        "",
        f"- Total committed: **${s['total_committed_usd']:,.0f}**",
        f"- Disbursed (ledger): **${s['total_disbursed_ledger_usd']:,.0f}** ({s['overall_pct_disbursed']}%)",
        f"- Disbursements: {s['disbursement_count']} (micro band: {s['micro_band_count']} / {s['micro_band_share']}%)",
        "",
        "## By category",
        "",
        "| Category | Committed | Ledger | % | Variance |",
        "|----------|----------:|-------:|--:|---------:|",
    ]
    for row in report["by_category"]:
        lines.append(
            f"| {row['category']} | ${row['committed_usd']:,.0f} | "
            f"${row['disbursed_ledger_usd']:,.0f} | {row['pct_of_commitment_ledger']}% | "
            f"${row['variance_declared_vs_ledger']:,.0f} |"
        )
    lines.extend(["", "## Flags", ""])
    if not report["flags"]:
        lines.append("_None_")
    else:
        for f in report["flags"]:
            lines.append(f"- **{f['severity']}** `{f['code']}` ({f.get('category')}) — {f['detail']}")
    lines.extend(
        [
            "",
            "---",
            f"_{report.get('ai_guardrail')}_",
            "_OCC-format narrative expansion is Phase 2; this is the quantitative spine._",
            "",
        ]
    )
    return "\n".join(lines)


def write_report(data: dict[str, Any] | None = None) -> tuple[Path, Path]:
    payload = data or load_commitment()
    report = build_report(payload)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    jpath = OUT_DIR / f"cba_report_{payload.get('institution_id')}_{stamp}.json"
    mpath = OUT_DIR / f"cba_report_{payload.get('institution_id')}_{stamp}.md"
    jpath.write_text(json.dumps(report, indent=2), encoding="utf-8")
    mpath.write_text(render_markdown(report), encoding="utf-8")
    latest_j = OUT_DIR / "latest_report.json"
    latest_m = OUT_DIR / "latest_report.md"
    latest_j.write_text(jpath.read_text(encoding="utf-8"), encoding="utf-8")
    latest_m.write_text(mpath.read_text(encoding="utf-8"), encoding="utf-8")
    return jpath, mpath


def main() -> int:
    j, m = write_report()
    print("OK", j)
    print("OK", m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
