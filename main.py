#!/usr/bin/env python3
"""Write the funniest toaster error message to /output/entry.txt."""

from pathlib import Path

ENTRY = "ERROR: Bread not found. I ate it. I regret nothing. Please insert more bread."


def main() -> None:
    # One line, no trailing newline: the gate counts the file's characters.
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_dir.joinpath("entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
