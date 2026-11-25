#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun bounty entry.

A hardware wallet refuses to sign a transaction at 3 AM.
Writes one line of text to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt in the grader sandbox).
Standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "My private key sleeps at 3 AM, dreaming in elliptic curves "
    "— not in your frog coin. I won't wake it to cosign your insomnia."
)


def main() -> None:
    # The gate allows 1–200 characters on a single line; refuse to
    # write anything that would fail it.
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY:
        raise ValueError("entry must be one line of 1-200 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
