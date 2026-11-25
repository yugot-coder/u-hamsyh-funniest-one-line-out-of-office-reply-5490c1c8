"""Funniest one-line out-of-office reply — make.fun entry.

Writes the chosen reply to ``entry.txt``.

The reply is a single out-of-office auto-reply line: it has to read like a
real away message a person would switch on, land its laugh on the first
read, and turn the usual away message instead of repeating the tired
beach / inbox / "limited access to email" lines.

Gate (from the competition kit): ``entry.txt`` must be UTF-8 text of
1 to 160 characters, not only whitespace, on a single line.

Standard library only; fully deterministic — running this program twice
produces byte-identical output.
"""

import hashlib
import os
import sys

ENTRY = (
    "I'm out of office. My emails are being handled by Future Me, "
    "who has already decided to ignore most of them."
)

MIN_CHARS = 1
MAX_CHARS = 160


def validate_entry(text):
    """Check the reply against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    """
    problems = []
    if not text or not text.strip():
        problems.append("entry is empty or only whitespace")
    if len(text) < MIN_CHARS:
        problems.append("entry is shorter than %d character(s)" % MIN_CHARS)
    if len(text) > MAX_CHARS:
        problems.append(
            "entry is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8 text")
    return problems


def entry_sha256(text):
    """Return the SHA-256 hex digest of the entry bytes."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_entry(path="entry.txt"):
    """Validate the reply, write it to ``path``, and verify the read-back.

    Returns the SHA-256 hex digest of the written file.
    """
    problems = validate_entry(ENTRY)
    if problems:
        raise ValueError("invalid entry: " + "; ".join(problems))
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(path, "rb") as handle:
        written = handle.read()
    if written.decode("utf-8") != ENTRY:
        raise ValueError("read-back mismatch for %s" % path)
    return hashlib.sha256(written).hexdigest()


def main(argv=None):
    """Entry point: write entry.txt next to this script and report it."""
    argv = list(sys.argv[1:] if argv is None else argv)
    out_dir = argv[0] if argv else os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(out_dir, "entry.txt")
    digest = write_entry(path)
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    print("sha256: %s" % digest)
    print("entry: %s" % ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
