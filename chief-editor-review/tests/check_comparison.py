#!/usr/bin/env python3
"""Synthetic behavioural canary: selection, endpoint ranks and undefined rates."""
import copy
import importlib.util
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("comparison_data", ROOT / "scripts/comparison_data.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
f = json.loads((ROOT / "tests/fixtures/presentation-comparison.json").read_text())
data, prev, cur, focal = f["monthly"], f["previous"], f["current"], f["focal"]
result = module.select_median_mover(data, cur, prev, focal)
assert result["selected"]["page"] == "Example Beta"
assert abs(result["selected"]["percentage_change"] - 80) < 1e-8
assert result["direction"] == "largest_increase"
# Largest percentage improvement is distinct from the highest absolute median.
assert module.rank_latest(data, cur, "median")[0]["page"] == "Example Gamma"
assert data["Example Beta"][cur]["total"] < data["Example Beta"][prev]["total"]
assert [r["page"] for r in module.rank_latest(data, cur, "median")] == ["Example Gamma", focal, "Example Beta", "Example Delta"]
assert [r["page"] for r in module.rank_latest(data, cur, "total")] == ["Example Gamma", "Example Beta", focal, "Example Delta"]
assert [r["page"] for r in module.rank_latest(data, cur, "total", [focal, "Example Delta"])] == [focal, "Example Delta"]
zero = copy.deepcopy(data)
zero["Example Beta"][prev]["median"] = 0
result = module.select_median_mover(zero, cur, prev, focal)
assert result["selected"]["page"] == "Example Gamma"
assert result["unranked"][0]["page"] == "Example Beta"
negative = copy.deepcopy(data)
for page in negative:
    negative[page][cur]["median"] = negative[page][prev]["median"] * 0.8
assert module.select_median_mover(negative, cur, prev, focal)["direction"] == "least_decline"
missing = {"Example Focal": data[focal], "Example Missing": {cur: {"median": 20}}}
assert module.select_median_mover(missing, cur, prev, focal)["selected"] is None
assert module.select_median_mover(missing, cur, prev, focal)["unranked"][0]["reason"] == "missing median"
print("PASS: strongest mover, metric-specific endpoint order, filtering, zero/missing bases, declining market")
