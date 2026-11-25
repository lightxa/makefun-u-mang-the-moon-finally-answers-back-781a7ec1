#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes exactly one line to /output/entry.txt: the Moon's reply to four
billion years of wishes, howls and late-night promises. Pure stdlib,
deterministic, no network at runtime.
"""

import os

LINE = (
    "Four billion years of wishes, howls and promises to change, "
    "and not one of you has ever wished me well. "
    "I am a rock. I am owed a card."
)


def main() -> None:
    text = LINE.strip()
    # Gate self-check, mirroring the sealed scorer: 1-240 chars, UTF-8,
    # not only whitespace, exactly one line.
    assert 1 <= len(text) <= 240, "line must be 1-240 characters"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "line must be single-line"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
