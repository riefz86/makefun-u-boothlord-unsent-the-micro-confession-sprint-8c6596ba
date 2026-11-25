#!/usr/bin/env python3
"""Entry for make.fun "Unsent: The Micro-Confession Sprint".

Writes one micro-confession in exactly two parts to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message itself,
one line written exactly as it was typed, with no explanation after it.
"""

import os

ENTRY = (
    "To: Maya\n"
    "I told everyone I was relieved when you left, but I still make coffee "
    "for two every morning and pour yours down the sink."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 260 characters,
    # and the message itself one line of at most 200 characters.
    assert 1 <= len(ENTRY) <= 260, len(ENTRY)
    assert len(ENTRY.split("\n")[1]) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
