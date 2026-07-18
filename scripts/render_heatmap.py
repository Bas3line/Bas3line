#!/usr/bin/env python3
"""Render contribution data as a self-contained animated terminal SVG."""

from datetime import date
import html
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data" / "contributions.json"
OUTPUT = ROOT / "contrib-heatmap.svg"
PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
CELL, STEP = 12, 15
PAD, LABEL, TITLE = 22, 30, 30


def level(count):
    if count == 0:
        return 0
    if count <= 3:
        return 1
    if count <= 8:
        return 2
    if count <= 15:
        return 3
    return 4


data = json.loads(DATA.read_text())
first = date.fromisoformat(data["days"][0]["date"])
column = [None] * ((first.weekday() + 1) % 7)
grid = []
for day in data["days"]:
    weekday = (date.fromisoformat(day["date"]).weekday() + 1) % 7
    column.extend([None] * max(0, weekday - len(column)))
    column.append(day)
    if len(column) == 7:
        grid.append(column)
        column = []
if column:
    grid.append(column + [None] * (7 - len(column)))

width = PAD * 2 + LABEL + len(grid) * STEP
grid_top = TITLE + 20
grid_left = PAD + LABEL
height = grid_top + 7 * STEP + 91
parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">',
    '<style>@keyframes reveal{to{opacity:1;transform:translateY(0)}}.day{opacity:0;transform:translateY(-6px);animation:reveal .42s cubic-bezier(.2,.8,.2,1) forwards}</style>',
    '<defs><linearGradient id="bg" x2="0" y2="1"><stop stop-color="#0d1420"/><stop offset="1" stop-color="#0a0e14"/></linearGradient></defs>',
    f'<rect width="{width}" height="{height}" rx="12" fill="url(#bg)"/><rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="12" fill="none" stroke="#1f6feb" stroke-opacity=".55"/>',
    f'<path d="M0 {TITLE}H{width}" stroke="#1f6feb" stroke-opacity=".35"/>',
]
for index, color in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")):
    parts.append(f'<circle cx="{PAD + index * 16}" cy="15" r="5" fill="{color}"/>')
parts.append(f'<text x="{width / 2}" y="19" fill="#7d8590" font-size="12" text-anchor="middle">bas3line@github: ~/contributions --graph</text>')

seen = set()
for col, week in enumerate(grid):
    for item in week:
        if item:
            value = date.fromisoformat(item["date"])
            key = (value.year, value.month)
            if key not in seen and value.day <= 7:
                seen.add(key)
                parts.append(f'<text x="{grid_left + col * STEP}" y="44" fill="#7d8590" font-size="10">{value:%b}</text>')
            break
for row, label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
    parts.append(f'<text x="{PAD}" y="{grid_top + row * STEP + 9}" fill="#7d8590" font-size="9">{label}</text>')

for col, week in enumerate(grid):
    for row, item in enumerate(week):
        if not item:
            continue
        count = item["count"]
        delay = col * .018 + row * .045
        title = html.escape(f'{item["date"]}: {count} contribution{"s" if count != 1 else ""}')
        parts.append(f'<rect class="day" x="{grid_left + col * STEP}" y="{grid_top + row * STEP}" width="{CELL}" height="{CELL}" rx="2.5" fill="{PALETTE[level(count)]}" style="animation-delay:{delay:.3f}s"><title>{title}</title></rect>')

footer = grid_top + 7 * STEP + 29
parts.extend([
    f'<path d="M0 {footer - 18}H{width}" stroke="#1f6feb" stroke-opacity=".25"/>',
    f'<text x="{PAD}" y="{footer}" fill="#7d8590" font-size="13"><tspan fill="#39d353" font-weight="700">{data["total_contributions"]:,}</tspan> contributions in the last year</text>',
    f'<text x="{width - PAD}" y="{footer}" fill="#7d8590" font-size="12" text-anchor="end">{data["range"]["start"]} &#8594; {data["range"]["end"]}</text>',
    f'<text x="{PAD}" y="{footer + 24}" fill="#7d8590" font-size="13">current streak <tspan fill="#22d3ee" font-weight="700">{data["current_streak"]} days</tspan>  &#183;  longest <tspan fill="#22d3ee" font-weight="700">{data["longest_streak"]} days</tspan></text>',
    f'<text x="{width - PAD}" y="{footer + 24}" fill="#7d8590" font-size="12" text-anchor="end">best day <tspan fill="#f2cc60" font-weight="700">{data["best_day"]["count"]}</tspan> on {data["best_day"]["date"]}</text>',
    '</svg>',
])
OUTPUT.write_text("".join(parts))
print(f"wrote {OUTPUT}")
