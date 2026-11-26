#!/usr/bin/env python3
"""One Line to Your Younger Self — writes the entry line to /output/entry.txt."""

import os

ENTRY = "Kid, stop waiting for the job to call back — the rent money is in the code you write at 2 a.m. on that cheap laptop."

def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
