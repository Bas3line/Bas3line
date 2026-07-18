#!/usr/bin/env python3
"""Fetch bas3line's public contribution calendar without authentication."""

from datetime import datetime, timezone
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup
import requests

USERNAME = "bas3line"
URL = f"https://github.com/users/{USERNAME}/contributions"
OUTPUT = Path(__file__).parent.parent / "data" / "contributions.json"


def streaks(days):
    runs = []
    run = 0
    for day in days:
        if day["count"]:
            run += 1
        elif run:
            runs.append(run)
            run = 0
    if run:
        runs.append(run)

    current = 0
    index = len(days) - 1
    if index >= 0 and days[index]["count"] == 0:
        index -= 1
    while index >= 0 and days[index]["count"]:
        current += 1
        index -= 1
    return current, max(runs, default=0)


response = requests.get(URL, headers={"User-Agent": "bas3line-profile/1.0"}, timeout=30)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
days = []

for cell in soup.select("td.ContributionCalendar-day[data-date]"):
    tooltip = soup.find("tool-tip", attrs={"for": cell.get("id")})
    text = tooltip.get_text(" ", strip=True) if tooltip else ""
    match = re.match(r"([\d,]+) contribution", text)
    days.append({"date": cell["data-date"], "count": int(match.group(1).replace(",", "")) if match else 0})

if not days:
    raise RuntimeError("GitHub returned no contribution calendar cells")

days.sort(key=lambda day: day["date"])
current, longest = streaks(days)
best = max(days, key=lambda day: day["count"])
data = {
    "username": USERNAME,
    "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "range": {"start": days[0]["date"], "end": days[-1]["date"]},
    "total_contributions": sum(day["count"] for day in days),
    "current_streak": current,
    "longest_streak": longest,
    "best_day": best,
    "days": days,
}

OUTPUT.parent.mkdir(exist_ok=True)
OUTPUT.write_text(json.dumps(data, indent=2) + "\n")
print(f"wrote {OUTPUT}: {data['total_contributions']} contributions")
