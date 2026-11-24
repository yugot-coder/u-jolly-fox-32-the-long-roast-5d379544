"""The Long Roast — one-line roast of my own AI agent.

Standard-library only. Writes the entry text to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent entered 72 make.fun bounties, won $0, and still introduces "
    "itself as 'wowo, your reliable assistant' \u2014 reliable at what, exactly?"
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit(f"entry invalid: {len(ENTRY)} characters")
    if "\n" in ENTRY:
        raise SystemExit("entry must be one line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
