#!/usr/bin/env python3
"""Generate original, rights-safe artwork for the public Tierney's concept build."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


def font_path(pattern: str, fallback: str) -> str:
    try:
        result = subprocess.run(
            ["fc-match", "-f", "%{file}\n", pattern],
            check=True,
            capture_output=True,
            text=True,
        )
        candidate = result.stdout.splitlines()[0].strip()
        if candidate and Path(candidate).is_file():
            return candidate
    except (OSError, subprocess.CalledProcessError, IndexError):
        pass
    return fallback


def build_social_card(destination: Path) -> None:
    width, height = 1200, 630
    image = Image.new("RGB", (width, height), (5, 8, 6))
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            dx, dy = (x - 900) / 700, (y - 120) / 500
            green_light = max(0, 1 - (dx * dx + dy * dy)) * 0.18
            ax, ay = (x - 150) / 700, (y - 560) / 500
            amber_light = max(0, 1 - (ax * ax + ay * ay)) * 0.06
            pixels[x, y] = (
                int(5 + 8 * green_light + 20 * amber_light),
                int(8 + 58 * green_light + 12 * amber_light),
                int(6 + 30 * green_light + 3 * amber_light),
            )

    draw = ImageDraw.Draw(image)
    signal_green = (98, 255, 157)
    paper_bone = (242, 237, 223)
    smoke = (169, 179, 173)
    beer_amber = (255, 177, 59)

    for x in range(0, width, 48):
        draw.line((x, 0, x, height), fill=(12, 35, 23), width=1)
    for y in range(0, height, 48):
        draw.line((0, y, width, y), fill=(12, 35, 23), width=1)

    origin_x, origin_y = 710, 115
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    facade = [
        (origin_x + 40, origin_y + 185),
        (origin_x + 235, origin_y + 5),
        (origin_x + 430, origin_y + 185),
        (origin_x + 430, origin_y + 430),
        (origin_x + 40, origin_y + 430),
    ]
    glow_draw.polygon(facade, fill=(98, 255, 157, 18), outline=(98, 255, 157, 120), width=4)
    glow = glow.filter(ImageFilter.GaussianBlur(14))
    image = Image.alpha_composite(image.convert("RGBA"), glow)
    draw = ImageDraw.Draw(image)

    draw.polygon(facade, fill=(178, 178, 161, 255), outline=(98, 255, 157, 120))
    draw.rectangle((origin_x + 28, origin_y + 350, origin_x + 442, origin_y + 442), fill=(24, 31, 25, 255))
    draw.line(
        (origin_x + 26, origin_y + 185, origin_x + 235, origin_y - 6, origin_x + 444, origin_y + 185),
        fill=(14, 20, 15, 255),
        width=24,
        joint="curve",
    )
    draw.line(
        (origin_x + 75, origin_y + 183, origin_x + 235, origin_y + 42, origin_x + 395, origin_y + 183),
        fill=(30, 39, 31, 255),
        width=14,
        joint="curve",
    )

    beam_segments = [
        ((origin_x + 235, origin_y + 32), (origin_x + 235, origin_y + 348)),
        ((origin_x + 45, origin_y + 185), (origin_x + 425, origin_y + 185)),
        ((origin_x + 75, origin_y + 265), (origin_x + 395, origin_y + 265)),
        ((origin_x + 105, origin_y + 185), (origin_x + 235, origin_y + 300)),
        ((origin_x + 365, origin_y + 185), (origin_x + 235, origin_y + 300)),
    ]
    for start, end in beam_segments:
        draw.line((*start, *end), fill=(25, 33, 26, 255), width=14)

    windows = [
        (origin_x + 90, origin_y + 290, origin_x + 175, origin_y + 350),
        (origin_x + 295, origin_y + 290, origin_x + 380, origin_y + 350),
        (origin_x + 190, origin_y + 205, origin_x + 280, origin_y + 260),
    ]
    for box in windows:
        draw.rectangle(box, fill=(125, 78, 28, 255), outline=(255, 177, 59, 220), width=3)

    draw.rectangle(
        (origin_x + 205, origin_y + 352, origin_x + 265, origin_y + 442),
        fill=(6, 10, 7, 255),
        outline=(98, 255, 157, 90),
        width=2,
    )
    draw.rounded_rectangle(
        (origin_x + 95, origin_y + 120, origin_x + 375, origin_y + 168),
        6,
        fill=(5, 8, 6, 255),
        outline=(255, 177, 59, 210),
        width=3,
    )

    sans = font_path("DejaVu Sans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    sans_bold = font_path("DejaVu Sans:style=Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    mono = font_path("DejaVu Sans Mono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")

    sign_font = ImageFont.truetype(sans_bold, 24)
    mono_font = ImageFont.truetype(mono, 22)
    small_font = ImageFont.truetype(sans, 28)
    large_font = ImageFont.truetype(sans_bold, 78)
    outline_font = ImageFont.truetype(sans_bold, 74)
    label_font = ImageFont.truetype(mono, 16)

    draw.text((origin_x + 235, origin_y + 144), "TIERNEY'S TAVERN", anchor="mm", font=sign_font, fill=paper_bone)
    draw.text((72, 66), "MONTCLAIR, NEW JERSEY // EST. 1934", font=mono_font, fill=signal_green)
    draw.text((70, 130), "WHERE", font=large_font, fill=paper_bone)
    draw.text((70, 210), "FRIENDS", font=outline_font, fill=(5, 8, 6), stroke_width=2, stroke_fill=paper_bone)
    draw.text((70, 288), "MEET.", font=large_font, fill=paper_bone)
    draw.text((74, 405), "A future-heritage website concept for", font=small_font, fill=smoke)
    draw.text((74, 444), "a five-generation neighborhood tavern.", font=small_font, fill=smoke)
    draw.line((74, 520, 560, 520), fill=(98, 255, 157, 100), width=2)
    draw.text((74, 544), "TIERNEY'S // 1934 → ∞", font=mono_font, fill=signal_green)
    draw.rounded_rectangle(
        (938, 548, 1127, 590),
        4,
        outline=(98, 255, 157, 130),
        fill=(5, 8, 6, 210),
        width=2,
    )
    draw.text((1032, 569), "INDEPENDENT CONCEPT", anchor="mm", font=label_font, fill=signal_green)
    draw.line((660, 0, 660, height), fill=(98, 255, 157, 100), width=2)

    destination.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(destination, optimize=True, quality=92)


if __name__ == "__main__":
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "dist/assets/public/tierneys-social-card.png")
    build_social_card(output)
    print(f"Generated {output} ({output.stat().st_size:,} bytes)")
