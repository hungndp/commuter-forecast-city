"""commuter-forecast-city — Charm the Commuter: Forecast a City That Isn't.

The line is a weather forecast for a city that does not exist,
written to make a bored commuter smile. Good morning, Yawnbury: 12
degrees, rain until nine, then sunshine — and the 8:15 bus is 3
minutes early, which the commuter's boss will never believe.
Concrete place name (Yawnbury), concrete weather and numbers (12
degrees, nine, 8:15, 3 minutes), a small reversal for the commuter.
The line is 138 characters, inside the 140-character cap, with no
dollar amount.
"""

import os

LINE = (
    "Good morning, Yawnbury: 12 degrees, rain until nine, then sunshine. "
    "The 8:15 bus is 3 minutes early, and your boss will never believe you."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
