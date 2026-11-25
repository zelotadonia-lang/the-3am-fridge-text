"""Entry for make.fun's "The 3AM Fridge Text" bounty.

The line is written in the voice of a small appliance filing a deadpan
shift report at 3am: it counts the owner's snacking as its own workload,
then lands the twist in the last words — 41 percent of the work, 0 percent
of the job description. Two hard numbers (41, 0) carry the joke; no
mothering, no setup, no follow-up. One line, one sentence, 87 characters.

Writes the line to /output/entry.txt.
"""

import os

LINE = "Your 3am snacking is now 41 percent of my workload and 0 percent of my job description."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise ValueError("entry must be 1 to 140 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
