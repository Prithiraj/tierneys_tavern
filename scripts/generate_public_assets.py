#!/usr/bin/env python3
"""Build web-ready real-photo assets for the Tierney's Tavern outreach site."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps


@dataclass(frozen=True)
class AssetSpec:
    source: str
    output: str
    size: tuple[int, int]
    centering: tuple[float, float] = (0.5, 0.5)
    credit: str = ""


ASSETS = (
    AssetSpec(
        "assets/reference/tierneys-exterior-montclair-girl.jpg",
        "exterior-hero",
        (1600, 1200),
        (0.5, 0.5),
        "The Montclair Girl",
    ),
    AssetSpec(
        "assets/reference/buddy-burger-mike-eats-nyc-burgers.jpg",
        "buddy-burger",
        (1200, 1200),
        (0.5, 0.5),
        "Mike Eats NYC Burgers",
    ),
    AssetSpec(
        "assets/reference/classic-cheeseburger-mike-eats-nyc-burgers.jpg",
        "classic-cheeseburger",
        (1200, 1200),
        (0.5, 0.5),
        "Mike Eats NYC Burgers",
    ),
    AssetSpec(
        "assets/reference/upstairs-performance-bizzboard.jpg",
        "upstairs-performance",
        (1400, 1050),
        (0.5, 0.5),
        "BiZZBoard reference",
    ),
    AssetSpec(
        "assets/reference/tierney-family-northjersey.jpg",
        "family-behind-bar",
        (1400, 933),
        (0.5, 0.5),
        "NorthJersey / Gannett",
    ),
    AssetSpec(
        "assets/reference/guinness-mural-mike-eats-nyc-burgers.jpg",
        "mural-stairs",
        (1200, 1200),
        (0.5, 0.5),
        "Mike Eats NYC Burgers",
    ),
)


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


def open_rgb(path: Path) -> Image.Image:
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
    return image


def build_variant(source: Path, output_dir: Path, spec: AssetSpec) -> dict[str, object]:
    image = open_rgb(source)
    target = ImageOps.fit(
        image,
        spec.size,
        method=Image.Resampling.LANCZOS,
        centering=spec.centering,
    )
    target = ImageEnhance.Contrast(target).enhance(1.025)

    jpg = output_dir / f"{spec.output}.jpg"
    webp = output_dir / f"{spec.output}.webp"
    target.save(jpg, "JPEG", quality=88, optimize=True, progressive=True, subsampling="4:2:0")
    target.save(webp, "WEBP", quality=83, method=6)

    return {
        "name": spec.output,
        "source": spec.source,
        "credit": spec.credit,
        "width": target.width,
        "height": target.height,
        "jpg_bytes": jpg.stat().st_size,
        "webp_bytes": webp.stat().st_size,
    }


def build_social_card(exterior_source: Path, destination: Path) -> None:
    width, height = 1200, 630
    photo = open_rgb(exterior_source)
    photo = ImageOps.fit(
        photo,
        (width, height),
        method=Image.Resampling.LANCZOS,
        centering=(0.58, 0.48),
    )
    photo = ImageEnhance.Color(photo).enhance(0.78)
    photo = ImageEnhance.Contrast(photo).enhance(1.06)
    photo = ImageEnhance.Brightness(photo).enhance(0.72).convert("RGBA")

    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    overlay_px = overlay.load()
    for y in range(height):
        for x in range(width):
            horizontal = max(0.0, min(1.0, 1.16 - x / 760))
            vertical = max(0.0, min(1.0, (y / height - 0.60) * 2.0))
            alpha = int(25 + 202 * horizontal + 72 * vertical)
            overlay_px[x, y] = (5, 8, 6, min(alpha, 238))

    image = Image.alpha_composite(photo, overlay)

    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    glow_draw.ellipse((660, 30, 1260, 650), fill=(13, 81, 52, 76))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    image = Image.alpha_composite(image, glow)

    draw = ImageDraw.Draw(image)
    signal_green = (98, 255, 157)
    paper_bone = (242, 237, 223)
    smoke = (191, 201, 195)

    for x in range(0, width, 48):
        draw.line((x, 0, x, height), fill=(98, 255, 157, 18), width=1)
    for y in range(0, height, 48):
        draw.line((0, y, width, y), fill=(98, 255, 157, 13), width=1)
    draw.line((0, 505, width, 505), fill=(98, 255, 157, 120), width=2)
    draw.line((735, 0, 735, height), fill=(98, 255, 157, 70), width=1)

    sans = font_path("DejaVu Sans", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    sans_bold = font_path(
        "DejaVu Sans:style=Bold",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    )
    mono = font_path(
        "DejaVu Sans Mono",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    )

    label_font = ImageFont.truetype(mono, 20)
    title_font = ImageFont.truetype(sans_bold, 78)
    outline_font = ImageFont.truetype(sans_bold, 72)
    body_font = ImageFont.truetype(sans, 27)
    tiny_font = ImageFont.truetype(mono, 14)

    draw.text((66, 58), "MONTCLAIR, NEW JERSEY // EST. 1934", font=label_font, fill=signal_green)
    draw.text((64, 126), "WHERE", font=title_font, fill=paper_bone)
    draw.text(
        (64, 204),
        "FRIENDS",
        font=outline_font,
        fill=(5, 8, 6),
        stroke_width=2,
        stroke_fill=paper_bone,
    )
    draw.text((64, 280), "MEET.", font=title_font, fill=paper_bone)
    draw.text((68, 402), "A real-photo, mobile-first website concept", font=body_font, fill=smoke)
    draw.text((68, 440), "for a five-generation neighborhood tavern.", font=body_font, fill=smoke)
    draw.text((68, 541), "TIERNEY'S // 1934 → ∞", font=label_font, fill=signal_green)
    draw.rounded_rectangle((930, 548, 1135, 590), 4, fill=(5, 8, 6, 210), outline=(98, 255, 157, 150), width=2)
    draw.text((1032, 569), "INDEPENDENT CONCEPT", anchor="mm", font=tiny_font, fill=signal_green)
    draw.text((824, 608), "Exterior photo: The Montclair Girl", font=tiny_font, fill=(215, 221, 217))

    destination.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(destination, "JPEG", quality=90, optimize=True, progressive=True)


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("Usage: generate_public_assets.py <repository-root> <dist-root>")

    root = Path(sys.argv[1]).resolve()
    dist = Path(sys.argv[2]).resolve()
    image_output = dist / "assets" / "images"
    public_output = dist / "assets" / "public"
    image_output.mkdir(parents=True, exist_ok=True)
    public_output.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, object]] = []
    for spec in ASSETS:
        source = root / spec.source
        if not source.is_file() or source.stat().st_size == 0:
            raise SystemExit(f"Missing real-photo source: {spec.source}")
        manifest.append(build_variant(source, image_output, spec))

    exterior = root / ASSETS[0].source
    build_social_card(exterior, public_output / "tierneys-social-card.jpg")
    (image_output / "credits.json").write_text(
        json.dumps({"usage": "attributed noncommercial concept", "images": manifest}, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Generated {len(manifest)} real-photo asset pairs and a photographic social card")


if __name__ == "__main__":
    main()
