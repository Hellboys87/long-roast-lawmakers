#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = (
    "The lawmakers writing 400-page bills to regulate artificial "
    "intelligence still print their emails, sign them in pen, and ask an "
    "intern to scan the signature back into a PDF."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
