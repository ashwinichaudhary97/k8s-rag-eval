#!/usr/bin/env python3
"""Build a SHA256 manifest of all Markdown files in the Kubernetes docs.

This manifest is the baseline against which corpus drift is detected.
It is committed to the repo so any future change to the docs produces
a detectable, reviewable diff.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

DOCS_DIR = Path("data/raw/k8s/content/en/docs")
OUTPUT = Path("corpus_manifest.json")


def hash_file(path: Path) -> str:
    """Return the hex SHA256 of a file's contents."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not DOCS_DIR.exists():
        print(f"ERROR: docs directory not found: {DOCS_DIR}")
        return 1

    manifest: dict[str, str] = {}
    for path in sorted(DOCS_DIR.rglob("*.md")):
        rel = str(path.relative_to(DOCS_DIR)).replace("\\", "/")
        manifest[rel] = hash_file(path)

    OUTPUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {len(manifest)} file hashes to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
