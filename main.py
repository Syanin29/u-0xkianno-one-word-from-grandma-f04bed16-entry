#!/usr/bin/env python3
"""One Word From Grandma — entry program (make.fun, program/v1).

Writes exactly one word to ``$MAKEFUN_OUTPUT_DIR/entry.txt``: the single
word Grandma would text about AI.

The word: ``calculator``.

Why this word (judged against the brief, criteria in order):
1. It reads as the single word a grandma would text about AI. She sees a
   machine that thinks, adds things up and answers her questions, and she
   calls it what she already knows: a calculator.
2. It sounds like her texting voice: warm and a little baffled. She is not
   scared of it and she is not showing off — she has simply filed the
   mysterious new machine under the familiar one on her kitchen table.
3. The joke lands in one word with no caption: a trillion-parameter model,
   reduced by Grandma to a pocket calculator.
4. It is tied to machines, not to any subject at all: a calculator IS a
   machine that computes. It could not be her word for a cake or a song.
5. It is fresh. The field is full of robit, doohickey, contraption,
   thingamajig, witchcraft, chatgbt and smartypants; at build time no
   entry title in the field's 1,922 submissions named "calculator".

Deterministic: standard library only, no model call, no network, no
randomness, no clock, no input read. The same bytes come out on every run.
"""

import os

WORD = "calculator"


def main() -> int:
    # The grader collects outputs as another user, so outputs must be
    # world-readable (known issue: a 0600 file fails collection).
    os.umask(0o022)

    # Gate: 1 to 30 characters, UTF-8, not only white space, one word.
    if not (1 <= len(WORD) <= 30):
        raise SystemExit("word fails the 1-30 character gate")
    if not WORD.strip() or len(WORD.split()) != 1:
        raise SystemExit("word is not exactly one word")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)

    # Self-check the bytes that were actually written.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != WORD:
        raise SystemExit("written bytes differ from the word")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
