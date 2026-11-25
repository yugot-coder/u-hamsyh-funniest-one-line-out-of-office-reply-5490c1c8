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
    """Validate the reply, write it to ``path``, and verify byte-exactly.

    The read-back must have the same byte length as the encoded entry
    (no trailing newline may sneak in), be byte-identical to it, and
    hash to the same SHA-256 digest. Returns the digest.
    """
    problems = validate_entry(ENTRY)
    if problems:
        raise ValueError("invalid entry: " + "; ".join(problems))
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(path, "rb") as handle:
        written = handle.read()
    intended = ENTRY.encode("utf-8")
    if len(written) != len(intended):
        raise ValueError("read-back byte length mismatch for %s" % path)
    if written != intended:
        raise ValueError("read-back mismatch for %s" % path)
    if hashlib.sha256(written).hexdigest() != entry_sha256(ENTRY):
        raise ValueError("read-back digest mismatch for %s" % path)
    return hashlib.sha256(written).hexdigest()


def main(argv=None):
    """Entry point: write entry.txt and report it.

    Destination: argv[0] if given, else $MAKEFUN_OUTPUT_DIR, else the
    directory next to this script.
    """
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv:
        out_dir = argv[0]
    elif os.environ.get("MAKEFUN_OUTPUT_DIR"):
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    else:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    digest = write_entry(path)
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    print("sha256: %s" % digest)
    print("entry: %s" % ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
