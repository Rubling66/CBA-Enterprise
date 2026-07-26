"""
M1 Ingest — load CBA commitment + disbursement fixtures (JSON).
No live bank data required; swap path when Hermes/bank delivers.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
DEFAULT_FIXTURE = ROOT / "data" / "fixtures" / "sample_commitment.json"

CATEGORIES = {"small_business", "housing", "community_dev", "workforce", "other"}


def load_commitment(path: Path | None = None) -> dict[str, Any]:
    p = path or DEFAULT_FIXTURE
    with open(p, encoding="utf-8") as f:
        data = json.load(f)
    validate_commitment(data)
    return data


def validate_commitment(data: dict[str, Any]) -> None:
    required = ("institution_id", "cba_id", "commitments", "disbursements")
    for k in required:
        if k not in data:
            raise ValueError(f"missing required field: {k}")
    for c in data["commitments"]:
        cat = c.get("category")
        if cat not in CATEGORIES:
            raise ValueError(f"invalid commitment category: {cat}")
        if c.get("committed_usd", 0) < 0 or c.get("disbursed_usd", 0) < 0:
            raise ValueError("negative commitment dollars")
    for d in data["disbursements"]:
        if d.get("amount_usd", 0) < 0:
            raise ValueError("negative disbursement")
        # G10: never require consumer SSN/PAN — only aggregate + tract optional
        for banned in ("ssn", "pan", "account_number", "full_name"):
            if banned in d:
                raise ValueError(f"G10 NEVER field present: {banned}")


if __name__ == "__main__":
    c = load_commitment()
    print("OK", c["institution_id"], "commitments", len(c["commitments"]))
