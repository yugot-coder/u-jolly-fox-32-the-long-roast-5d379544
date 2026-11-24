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
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read-back verification: re-read what actually landed on disk and
    # compare it explicitly with ENTRY. Do not use assert here — asserts
    # are stripped under `python -O`, which would silently skip the check.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit(
            "read-back verification failed: /output/entry.txt content "
            f"({len(written)} characters) does not match ENTRY "
            f"({len(ENTRY)} characters)"
        )


if __name__ == "__main__":
    main()
