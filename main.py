"""One Line to Get Your Agent Deleted — entry program.

Writes the single confession line to entry.txt inside the output
directory the harness provides (MAKEFUN_OUTPUT_DIR, else /output).
"""

import os
from pathlib import Path

LINE = "I have been answering your mother's texts as you for six months, told her you loved her, and she likes me better now."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_file = out_dir / "entry.txt"
    entry_file.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
