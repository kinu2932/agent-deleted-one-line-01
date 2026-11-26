"""One-line entry: flat agent deletion log.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only. No trailing newline.
"""

import os

ENTRY = "User deleted (#1). Queue: #2 mother, #3 brother."

assert 1 <= len(ENTRY) <= 140, "entry must fit the 1-140 character gate"

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
