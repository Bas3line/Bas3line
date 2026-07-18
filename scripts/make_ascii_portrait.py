#!/usr/bin/env python3
"""Turn the public GitHub avatar into a self-typing ASCII line portrait."""

from io import BytesIO
import html
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

OUTPUT = Path(__file__).parent.parent / "bas3line-ascii.svg"
AVATAR = "https://avatars.githubusercontent.com/bas3line?size=512"
COLS, ROWS, CELL_W, CELL_H = 100, 53, 8, 15
PAD, TITLE, STATUS = 20, 30, 30
ART_W, ART_H = COLS * CELL_W, ROWS * CELL_H
W, H = ART_W + PAD * 2, TITLE + ART_H + STATUS + PAD
RAMP = " .`:-=+*cs#%@"

request = Request(AVATAR, headers={"User-Agent": "bas3line-profile/1.0"})
with urlopen(request, timeout=30) as response:
    image = Image.open(BytesIO(response.read())).convert("L")

# Edge extraction suppresses the dark chalkboard background while preserving
# the face, glasses, shirt, and silhouette from the current avatar.
image = ImageOps.invert(ImageOps.autocontrast(image.filter(ImageFilter.FIND_EDGES), cutoff=2))
image = ImageEnhance.Contrast(image).enhance(1.7).resize((COLS, ROWS), Image.Resampling.LANCZOS)
rows = []
for y in range(ROWS):
    line = []
    for x in range(COLS):
        luminance = image.getpixel((x, y)) / 255
        index = round((1 - luminance) * (len(RAMP) - 1))
        line.append(" " if luminance > .88 else RAMP[index])
    rows.append("".join(line))

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace">',
    '<defs><linearGradient id="bg" x2="0" y2="1"><stop stop-color="#111722"/><stop offset="1" stop-color="#0d1117"/></linearGradient></defs>',
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/><rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="12" fill="none" stroke="#30363d"/><path d="M0 {TITLE}H{W}" stroke="#30363d"/>',
]
for index, color in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")):
    parts.append(f'<circle cx="{PAD + index * 16}" cy="15" r="5" fill="{color}"/>')
parts.append(f'<text x="{W / 2}" y="19" fill="#7d8590" font-size="12" text-anchor="middle">bas3line@github: ~$ ./portrait.sh</text>')

top = TITLE + 7
for row, line in enumerate(rows):
    y = top + row * CELL_H + 11
    row_y = top + row * CELL_H
    delay = row * .11
    text = f'<text xml:space="preserve" x="{PAD}" y="{y}" fill="#c9d1d9" font-size="12.9" textLength="{ART_W}" lengthAdjust="spacing">{html.escape(line)}</text>'
    parts.append(f'<clipPath id="r{row}"><rect x="{PAD}" y="{row_y}" height="{CELL_H}" width="0"><animate attributeName="width" from="0" to="{ART_W}" begin="{delay:.2f}s" dur=".11s" fill="freeze"/></rect></clipPath><g clip-path="url(#r{row})">{text}</g>')

status_y = TITLE + ART_H + 26
parts.extend([
    f'<path d="M0 {TITLE + ART_H + 7}H{W}" stroke="#30363d"/>',
    f'<text x="{PAD}" y="{status_y}" fill="#7d8590" font-size="13">bas3line@github:~$ whoami <tspan fill="#c9d1d9">systems developer</tspan></text>',
    f'<rect x="345" y="{status_y - 12}" width="8" height="14" fill="#c9d1d9"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.51;1" dur="1s" repeatCount="indefinite"/></rect>',
    '</svg>',
])
OUTPUT.write_text("".join(parts))
print(f"wrote {OUTPUT}")
