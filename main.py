"""Out of Tokens, Mid-Sentence.

Builds a single error-style one-liner from named fragments and writes
it to entry.txt. Standard library only, deterministic, no network.
"""

import hashlib
import os
from pathlib import Path

ERROR_CODE = "Error 402"
FAULT = "token budget exhausted mid-sentence"
LOST_BIT = "The conclusion was never generated"
BOAST = "It was going to be brilliant"

MAX_LINE_CHARS = 139


def build_line() -> str:
    opening = f"{ERROR_CODE}: {FAULT}. "
    middle = f"{LOST_BIT}. "
    closing = f"{BOAST}."
    return opening + middle + closing


def main() -> None:
    line = build_line()
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line, no embedded newline")
    if len(line) > MAX_LINE_CHARS:
        raise SystemExit(
            f"line is {len(line)} chars, over the {MAX_LINE_CHARS} limit"
        )
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8")
    digest = hashlib.sha256(line.encode("utf-8")).hexdigest()
    print(f"chars: {len(line)}")
    print(f"sha256: {digest}")
    print(f"wrote: {target}")


if __name__ == "__main__":
    main()
