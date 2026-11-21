#!/usr/bin/env python3
"""Write one original one-line joke about working beside AI coding agents
to /output/entry.txt (or $OUTPUT_DIR/entry.txt for local testing).

The program is deliberately deterministic: the joke is a fixed string, so
every run in the sandbox produces the same valid entry.
"""

import os
import sys

MAX_CODE_POINTS = 280

JOKE = (
    "My AI agent fixed the demo bug by deleting the feature "
    "\u2014 then offered to do the same to the rest of the app."
)


def main() -> int:
    text = JOKE.strip()
    if not text or text.isspace():
        print("joke is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CODE_POINTS:
        print("joke exceeds 280 code points", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("joke must be one line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify what actually landed on disk: valid UTF-8,
    # 1-280 code points, a single line, not only whitespace.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("written entry differs from the joke", file=sys.stderr)
        return 1
    if not written or written.isspace() or len(written) > MAX_CODE_POINTS:
        print("written entry fails the gate", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
