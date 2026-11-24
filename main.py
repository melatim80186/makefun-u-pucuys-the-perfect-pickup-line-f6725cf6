#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes the single chosen pickup line to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import hashlib
import os

# The line, split into its two beats: the setup states the machine's
# everyday chore, the punch turns it into the compliment.
SETUP = "Every CAPTCHA asks me to prove I'm human"
PUNCH = "you're the first person who makes me want to pass."
ENTRY = SETUP + " \u2014 " + PUNCH
# Sealed-scorer gate: /output/entry.txt must be UTF-8 text, 1-200 chars,
# not only whitespace. MAX_CHARS pins the upper bound here so the
# pre-write self-check enforces exactly the gate's limit.
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def self_check(line: str) -> None:
    assert 1 <= len(line) <= MAX_CHARS, "line must be 1-%d chars, got %d" % (MAX_CHARS, len(line))
    assert line == line.strip(), "no leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "must be a single line"
    assert line.strip(), "must not be only whitespace"
    line.encode("utf-8")


def main() -> None:
    self_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "post-write bytes differ"
    print("wrote %d chars to %s" % (len(ENTRY), OUTPUT_PATH))
    print("sha256: %s" % hashlib.sha256(written).hexdigest())


if __name__ == "__main__":
    main()
