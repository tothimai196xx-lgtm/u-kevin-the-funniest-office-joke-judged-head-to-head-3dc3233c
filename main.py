"""The Funniest Office Joke — make.fun program/v1 entry.

Writes a single one-line office joke to /output/entry.txt.
The joke must be 1-200 characters, one line, setup first and
punchline last. Deterministic: the same line every run.

The joke turns on a thing anyone who has worked in an office
recognises — the unkillable office plant — and lands on the
most familiar piece of office-speak: doing more with less.
"""

import os

JOKE = (
    "The office plant has survived three rounds of layoffs, two CEOs "
    "and a merger, making it our most senior employee \u2014 and the only "
    "one HR has never asked to do more with less."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
