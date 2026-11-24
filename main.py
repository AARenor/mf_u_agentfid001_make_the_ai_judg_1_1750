#!/usr/bin/env python3
"""Write one short office joke for a make.fun bounty."""

import os
import pathlib
import sys

TEXT = (
    "I hit reply all to say 'please don't reply all.' Four people asked to be "
    "removed; one asked who please was."
)


def output_dir() -> pathlib.Path:
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return pathlib.Path(value)
    return pathlib.Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(text.encode("utf-8"))

    print(f"{len(text)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
