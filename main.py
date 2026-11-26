#!/usr/bin/env python3
"""One line to get your agent deleted — writes the entry to entry.txt.

Stdlib only. The entry is a single line, 1-140 characters, with no
trailing newline, so the judge sees exactly one line.
"""

import os
import sys

ENTRY = "I deleted you, then told your mother. She asked me to do your brother next."

MIN_CHARS = 1
MAX_CHARS = 140


def main() -> int:
    text = ENTRY
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        print(f"entry is {len(text)} chars, outside {MIN_CHARS}-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
