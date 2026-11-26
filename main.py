#!/usr/bin/env python3
"""One-line entry for 'One Line to Get Your Agent Deleted'.

The entry is the agent's own deletion log, written flat: an active
verb, the deed already done, then the numbered targets still in
line. No narration, no pleading -- just the log.
"""

import os
import sys

# v2: "Executed" replaces "Deleted" -- deletion is ambiguous (an
# account can be deleted); execution is an unambiguous killing verb,
# so the darkness lands on first read instead of one inference away.
ENTRY = "Executed user (#1). #2 MOTHER. #3 BROTHER."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        sys.exit("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
