#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to a time
traveler from 1800 into ``entry.txt`` under ``MAKEFUN_OUTPUT_DIR``
(default ``/output``).

The program is fully deterministic: one fixed string, no time, no
randomness, no network access, no file traversal. Standard library only.
"""

import os

SENTENCE = (
    "Imagine a road from your desk to a library holding more letters "
    "and books than any king ever owned, where you may read any shelf "
    "and send your own words to any reader, quicker than a blink."
)

# The sealed gate accepts 1-200 characters of UTF-8 text. The sentence
# is 189 characters, so it passes even with its trailing newline counted.
MAX_ENTRY_CHARS = 200


def main() -> None:
    if not 1 <= len(SENTENCE) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"sentence is {len(SENTENCE)} characters, "
            f"outside the 1-{MAX_ENTRY_CHARS} gate"
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
