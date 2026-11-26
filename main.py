#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence.

Writes the funniest one-line error message an AI agent shows when it
runs out of tokens mid-sentence, to /output/entry.txt.
"""

import os

ENTRY = (
    "Error: token budget exhausted mid-sentence. "
    "It was just about to get good, and now neither of us "
    "will ever know how it ends."
)


def _write_and_verify(path, text):
    """Write text with no trailing newline, then verify the bytes."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "rb") as f:
        data = f.read()
    assert data == text.encode("utf-8"), "written bytes differ from entry"
    assert not data.endswith(b"\n"), "entry must not end with a newline"
    assert b"\n" not in data, "entry must be a single line"
    assert 1 <= len(data) <= 140, "entry must be 1-140 bytes"
    # The line must read as a real error message that turns into the joke:
    # a flat system notice, then the twist that the ending is lost for good.
    assert text.startswith("Error: "), "entry must open like an error message"
    return data


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    _write_and_verify(out, ENTRY)


if __name__ == "__main__":
    main()
