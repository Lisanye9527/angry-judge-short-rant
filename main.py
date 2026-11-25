"""Entry for make.fun bounty "Angry Judge: The Short Rant Contest".

Writes one short rant -- about the smoke alarm whose battery only ever
dies at 3 a.m. -- to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output`` when
the variable is unset, matching the grader container).

The text is a constant, so the program is deterministic: every run
writes exactly the same bytes. Before writing, the program checks the
text against the bounty gate (UTF-8 text of 1 to 400 characters, not
only white space) and fails loudly if it ever drifts out of bounds.

Run it from the repository root, for example:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

RANT = (
    "My smoke alarm's battery only dies at 3 a.m. It chirps, waits "
    "until I am almost asleep again, then chirps \u2014 all night. Stand "
    "under it to find the guilty one and it goes silent. Nobody alive "
    "owns a spare 9-volt battery. It is not a safety device. It is a "
    "tiny landlord in my ceiling, collecting rent in sleep."
)

MAX_CHARS = 400


def main() -> int:
    text = RANT
    if not text.strip():
        print("error: the rant is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: the rant is {len(text)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip() or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(text, encoding="utf-8")
    written = dest.read_text(encoding="utf-8")
    if written != text:
        print("error: written text differs from the rant", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
