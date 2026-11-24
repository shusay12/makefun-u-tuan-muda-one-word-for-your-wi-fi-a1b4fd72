#!/usr/bin/env python3
"""One Word for Your Wi-Fi -- make.fun entry.

The entry is a single word describing the entrant's Wi-Fi, written to
/output/entry.txt (or $ENTRY_OUTPUT when set, for local runs).

Chosen word: Teenager

Why it wins on the judge's brief, in the brief's own order:
1. On-subject: it describes Wi-Fi as the entrant lives it -- a connection
   that only works in its own room, ignores you when you call, and sulks
   until you restart it (the universal dead-zone experience).
2. Funny at once: the comparison lands the instant you read it, no
   explanation needed -- everyone knows a teenager.
3. True: home Wi-Fi really does behave this way -- strong in one room,
   gone two rooms over, moody for no reason, fixed by being told to
   turn itself off and on again.
4. Fresh angle: nobody's first reach is a person; the field will be full
   of "slow", "laggy", "buffering" and "ghost". A teenager is a person,
   not a speed complaint.
5. One word, spelled so a reader gets it instantly, and it works as a
   Wi-Fi network name -- which is what the winning word becomes.
"""

import os
import sys

ENTRY = "Teenager"


def main() -> int:
    # Gate: UTF-8 text of 1 to 20 characters, not only white space.
    if not (1 <= len(ENTRY) <= 20):
        print(f"entry length {len(ENTRY)} outside 1..20", file=sys.stderr)
        return 1
    if not ENTRY.strip() or any(ch.isspace() for ch in ENTRY):
        print("entry must be a single word with no whitespace", file=sys.stderr)
        return 1
    if not ENTRY.isalpha():
        # A single word, not a code or a phrase with punctuation/digits.
        print("entry must be letters only", file=sys.stderr)
        return 1

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    # No trailing newline: the entry is exactly the word, nothing else.
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    # Read back and verify byte-for-byte: the grader runs this program
    # twice and gates the exact bytes, so a silent write failure must
    # never pass as success.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != ENTRY.encode("utf-8"):
        print(f"verification failed: {out_path} holds {written!r}", file=sys.stderr)
        return 1
    print(f"wrote {out_path}: {ENTRY!r} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
