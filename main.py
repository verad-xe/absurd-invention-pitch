#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single original sentence pitching a ridiculous invention that
fixes a tiny everyday annoyance: a houseplant that emails your boss a
sick note every time you forget to water it.
"""

import os

ENTRY = (
    "A houseplant that emails your boss a sick note every time you forget "
    "to water it, so your neglect finally has consequences \u2014 just not "
    "for you."
)


def check_gate(entry: str) -> None:
    """Self-check the bounty gate: 1-220 UTF-8 chars, exactly one sentence.

    The bounty scores a single sentence, so a gate breach (too long, or a
    second sentence sneaking in) would fail the entry outright. Checking
    before writing means a bad ENTRY can never be submitted silently.
    """
    if not 1 <= len(entry) <= 220:
        raise ValueError(f"entry must be 1-220 chars, got {len(entry)}")
    # Exactly one sentence: a single terminal period, no other terminators.
    if entry.count(".") != 1 or not entry.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if any(c in entry for c in "!?"):
        raise ValueError("entry must not contain extra sentence terminators")


def main() -> None:
    check_gate(ENTRY)
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
