#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

make.fun competition u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2
(harness program/v1).

The entry is a single line: a museum placard for an ordinary office object,
written as if the object were an ancient artifact dug from a lost
civilisation. The grader runs this program as ``python3 -P -s main.py``
with no network, and reads ``/output/entry.txt``. The gate accepts UTF-8
text of 1 to 180 characters, not only white space.

The placard below was chosen by a local pairwise tournament judged by the
competition's own judge model (z-ai/glm-5.3-flash) running the published
brief verbatim: six original drafts, every pair judged in both orders
(30 judge calls). The hole punch won (mean game score 0.710, 4 wins from
5 games): the judge praised the invented history — forty thousand holes
punched in the founding charter, one per objection the minutes never
recorded — and the deadpan donor line from Records.
"""

import os
import sys

# The placard. 148 characters: one line, catalogue date, material,
# the conceit (a perforator that dissented against the charter) and
# provenance (donated by Records).
PLACARD = (
    "Perforator, c. 1998. Steel. It punched 40,000 holes in the founding "
    "charter, one for every objection the minutes never recorded. "
    "Donated by Records."
)

MAX_CHARS = 180


def check_gate(text: str) -> str | None:
    """Return an error message if the placard fails the gate, else None."""
    if not (1 <= len(text) <= MAX_CHARS):
        return f"placard is {len(text)} chars, gate allows 1-{MAX_CHARS}"
    if not text.strip():
        return "placard is only white space"
    if "\n" in text or "\r" in text:
        return "placard must be one line"
    text.encode("utf-8")
    return None


def main() -> int:
    # Gate, mirrored locally: 1 to 180 characters, not only white space,
    # a single line, valid UTF-8.
    error = check_gate(PLACARD)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    text = PLACARD

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
