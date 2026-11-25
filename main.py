#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse, in its own voice, for sending the
driver down the wrong road, to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space, exactly one line, no setup, no dialogue tags.
"""

import os

EXCUSE = (
    "The map called that lake a shortcut and I believed it \u2014 "
    "in my defence, the lake had a name, a postcode, "
    "and more confidence than me."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    line = EXCUSE.strip()
    assert line, "excuse must not be empty"
    assert "\n" not in line and "\r" not in line, "excuse must be one line"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"excuse must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.strip(), "excuse must not be only white space"

    print(line)

    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError as exc:
        raise SystemExit(f"failed to write {OUTPUT_PATH}: {exc}") from exc

    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "written entry does not match the excuse"


if __name__ == "__main__":
    main()
