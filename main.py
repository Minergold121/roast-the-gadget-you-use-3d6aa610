"""Write one roast line to /output/entry.txt.

One fixed line, no randomness, no time, no network, stdlib only.
The roast: a phone whose face unlock seems to recognise everyone
except its owner first thing in the morning.
"""

import os

ROAST = "My phone's face unlock recognizes my cat, a blurry photo, and me at 2 a.m. \u2014 just never me, first thing in the morning, squinting."

# The harness reads exactly this path; the gate allows 1-200 characters.
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ROAST + "\n")


if __name__ == "__main__":
    main()
