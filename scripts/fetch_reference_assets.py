#!/usr/bin/env python3
"""Download the exact reference assets declared in ASSET_SOURCES.json.

The script deliberately has no placeholder or stock-image fallback. A missing,
HTML, undersized, or invalid image causes a non-zero exit so the repository
cannot silently claim that collection succeeded.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import urllib.error
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "ASSET_SOURCES.json"
CHECKSUM_PATH = ROOT / "assets" / "reference" / "SHA256SUMS.txt"

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36 "
    "TierneysTavernDesignResearch/1.0"
)


def normalized_content_type(value: str | None) -> str:
    return (value or "").split(";", 1)[0].strip().lower()


def image_signature(data: bytes) -> str | None:
    if data.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return "image/gif"
    if len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "image/webp"
    if len(data) >= 12 and data[4:8] == b"ftyp":
        if data[8:12] in {b"avif", b"avis"}:
            return "image/avif"
    return None


def fetch(asset: dict[str, object]) -> tuple[Path, str, int]:
    relative_path = Path(str(asset["path"]))
    target = ROOT / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)

    url = str(asset["download_url"])
    minimum_bytes = int(asset.get("minimum_bytes", 1))
    allowed_types = {
        normalized_content_type(str(item))
        for item in asset.get("allowed_types", [])
    }

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Referer": str(asset.get("source_page", url)),
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            header_type = normalized_content_type(response.headers.get("Content-Type"))
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError(f"{relative_path}: download failed: {exc}") from exc

    detected_type = image_signature(data)
    if detected_type is None:
        preview = data[:80].decode("utf-8", errors="replace").replace("\n", " ")
        raise RuntimeError(
            f"{relative_path}: response is not a recognized raster image; "
            f"content-type={header_type!r}, first-bytes={preview!r}"
        )

    if allowed_types and detected_type not in allowed_types:
        raise RuntimeError(
            f"{relative_path}: detected {detected_type}, expected one of "
            f"{sorted(allowed_types)}"
        )

    if len(data) < minimum_bytes:
        raise RuntimeError(
            f"{relative_path}: image is {len(data)} bytes; "
            f"minimum is {minimum_bytes}"
        )

    digest = hashlib.sha256(data).hexdigest()
    current = target.read_bytes() if target.exists() else None
    if current != data:
        with tempfile.NamedTemporaryFile(
            dir=target.parent, prefix=f".{target.name}.", delete=False
        ) as temp:
            temp.write(data)
            temp_path = Path(temp.name)
        os.replace(temp_path, target)

    return relative_path, digest, len(data)


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    assets = manifest.get("assets")
    if not isinstance(assets, list) or not assets:
        raise RuntimeError("ASSET_SOURCES.json contains no assets")

    results: list[tuple[Path, str, int]] = []
    failures: list[str] = []

    for raw_asset in assets:
        try:
            result = fetch(raw_asset)
            results.append(result)
            print(f"collected {result[0]} ({result[2]:,} bytes)")
        except Exception as exc:
            failures.append(str(exc))
            print(f"ERROR: {exc}", file=sys.stderr)

    if failures:
        print("\nAsset collection failed; no placeholders were written:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    CHECKSUM_PATH.parent.mkdir(parents=True, exist_ok=True)
    CHECKSUM_PATH.write_text(
        "".join(f"{digest}  {path.as_posix()}\n" for path, digest, _ in results),
        encoding="utf-8",
    )
    print(f"wrote {CHECKSUM_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
