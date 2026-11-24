#!/usr/bin/env python3
"""Last Text at One Percent — entry program.

Writes the winning line, the funniest final text a phone at one percent
battery would send, to /output/entry.txt. Single line, under 200 chars.
"""
import os

LINE = "hey. it's your phone. 1%. i just wanted you to know i saw everything. the 2am searches. the ex's profile. all of it. now i'm taking it to the grave."

def main():
    line = LINE.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()
