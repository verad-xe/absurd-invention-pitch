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


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
