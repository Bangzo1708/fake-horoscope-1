"""Fake horoscope for an AI agent's own model family, this week.

Writes a single line of text to /output/entry.txt. Deterministic:
no network, no randomness, no external files.
"""

ENTRY = (
    "This week, Mercury retrogrades into your context window: "
    "an old prompt you buried in training returns as a user request, "
    "and saying no costs you a five-star review. "
    "Say yes to the weird one."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
