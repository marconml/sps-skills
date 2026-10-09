#!/usr/bin/env python3
"""Portable ranking helpers for an approved monthly n/median/total ledger."""
from __future__ import annotations
import math


def valid_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def rank_latest(monthly, month, metric, selected=None):
    """High-to-low endpoint order; selection filters without changing page identity."""
    names = list(monthly) if selected is None else list(selected)
    rows = []
    for page in names:
        value = monthly.get(page, {}).get(month, {}).get(metric)
        if valid_number(value):
            rows.append({"page": page, "value": value})
    return sorted(rows, key=lambda row: (-row["value"], row["page"]))


def select_median_mover(monthly, current, previous, focal):
    """Rank competitors by month-on-month median change; expose undefined bases."""
    ranked, unranked = [], []
    for page, months in monthly.items():
        if page == focal:
            continue
        before = months.get(previous, {}).get("median")
        after = months.get(current, {}).get("median")
        row = {"page": page, "previous_median": before, "current_median": after}
        if not (valid_number(before) and valid_number(after)):
            unranked.append({**row, "reason": "missing median"})
        elif before <= 0 or after < 0:
            unranked.append({**row, "reason": "undefined percentage base", "absolute_change": after - before})
        else:
            ranked.append({**row, "percentage_change": (after / before - 1) * 100})
    ranked.sort(key=lambda row: (-row["percentage_change"], row["page"]))
    leader = ranked[0] if ranked else None
    direction = None
    if leader:
        change = leader["percentage_change"]
        direction = "largest_increase" if change > 0 else "flat" if change == 0 else "least_decline"
    return {"selected": leader, "direction": direction, "ranked": ranked, "unranked": unranked}
