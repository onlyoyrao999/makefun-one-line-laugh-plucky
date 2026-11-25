#!/usr/bin/env python3
"""One Line, One Laugh — a single funny line, written to /output/entry.txt."""

import os
import sys

LINE = "I asked my smart speaker for motivation. It paused, sighed, and said: 'Have you tried being someone else?'"
MAX_CHARS = 200


def validate(line):
    """The gate: one line, 1 to 200 characters, not only whitespace."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    return line


def main() -> None:
    line = validate(LINE)
    print(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read back and confirm what landed is exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        if f.read().strip() != line:
            print("verification failed: entry.txt does not match the line",
                  file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
