#!/usr/bin/env python3
"""The One-Line Laugh (u-ronigrv-the-one-line-laugh-7ccca46f).

Writes one funny line (at most 200 characters) to /output/entry.txt.
Python 3.13 standard library only. Deterministic: the same line every run.
"""

import os
import sys

# One funny line: an everyday truth (gadgets never fix lateness) with the
# surprise saved for the very last words. Rule of three: two soft positives,
# then the twist. "Exactly" sharpens the punch over "just" — the lamp changed
# nothing at all.
LINE = (
    "I replaced my alarm with a sunrise lamp, and now I wake up gently, "
    "peacefully, and exactly as late as before."
)


def main() -> None:
    output_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
