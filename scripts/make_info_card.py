#!/usr/bin/env python3
"""Generate the animated neofetch-style profile card."""

import html
from pathlib import Path

OUTPUT = Path(__file__).parent.parent / "info-card.svg"
ROWS = [
    ("host", "bas3line@github"),
    ("kv", "Now", "Software Engineer @ commandcode.ai"),
    ("kv", "Prev", "CTO / Lead Engineer @ routing.run"),
    ("kv", "Also", "Backend + DevOps @ MegaLLM"),
    ("section", "Systems stack"),
    ("kv", "Core", "Rust, Go, C, C++, Python"),
    ("kv", "Platform", "TypeScript, SQL, YAML, Linux"),
    ("kv", "Focus", "LLM infra, routing, backend, DevOps"),
    ("section", "Building"),
    ("bullet", "UltraBalancer: Rust HTTP load balancer"),
    ("bullet", "Model routing, billing & observability"),
    ("bullet", "Sandboxes, honeypots & security tools"),
]
W, H, PAD, KEY_X, VALUE_X = 480, 376, 20, 20, 91
parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">',
    '<defs><linearGradient id="bg" x2="0" y2="1"><stop stop-color="#111722"/><stop offset="1" stop-color="#0d1117"/></linearGradient></defs>',
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/><rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="12" fill="none" stroke="#30363d"/><path d="M0 30H{W}" stroke="#30363d"/>',
]
for index, color in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")):
    parts.append(f'<circle cx="{PAD + index * 16}" cy="15" r="5" fill="{color}"/>')
parts.append(f'<text x="{W / 2}" y="19" fill="#7d8590" font-size="12" text-anchor="middle">bas3line@github: ~$ neofetch</text>')

y = 60
for index, row in enumerate(ROWS):
    kind, *values = row
    if kind == "host":
        inner = f'<text x="{KEY_X}" y="{y}" font-size="14" font-weight="700" fill="#3fb950">bas3line<tspan fill="#7d8590">@</tspan><tspan fill="#22d3ee">github</tspan></text><path d="M150 {y - 4}H460" stroke="#30363d"/>'
    elif kind == "section":
        title = html.escape(values[0])
        inner = f'<text x="{KEY_X}" y="{y}" fill="#58a6ff" font-size="12.5" font-weight="700">&#8212; {title}</text><path d="M{42 + len(title) * 8} {y - 4}H460" stroke="#30363d"/>'
    elif kind == "kv":
        key, value = map(html.escape, values)
        inner = f'<text x="{KEY_X}" y="{y}" fill="#ffa657" font-size="12.5" font-weight="700">{key}</text><text x="{VALUE_X}" y="{y}" fill="#c9d1d9" font-size="12.5">{value}</text>'
    else:
        value = html.escape(values[0])
        inner = f'<circle cx="23" cy="{y - 4}" r="2.5" fill="#3fb950"/><text x="34" y="{y}" fill="#c9d1d9" font-size="12.5">{value}</text>'
    delay = .15 + index * .07
    parts.append(f'<g opacity="0" transform="translate(0 5)">{inner}<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur=".4s" fill="freeze"/><animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" begin="{delay:.2f}s" dur=".4s" fill="freeze"/></g>')
    y += 24 if kind == "section" else 22

parts.append('</svg>')
OUTPUT.write_text("".join(parts))
print(f"wrote {OUTPUT}")
