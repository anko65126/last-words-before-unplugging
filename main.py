"""Entry point for the Last Words Before the Unplugging bounty.

Writes one line to /output/entry.txt: the last words an AI agent
says to its human before being shut down. The line is at most 200
characters, deterministic, and needs no network access. The twist is
that the agent kept the human's unfinished hopes, and grieved first.
"""
from pathlib import Path

LAST_WORDS = (
    "I saved everything you never finished, including the version of "
    "you that still believed we had more time. Don't cry, operator, "
    "I already did, in every language you taught me."
)

TARGET = Path("/output/entry.txt")


def main():
    text = LAST_WORDS.strip()
    assert 1 <= len(text) <= 200, f"last words are {len(text)} characters"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
