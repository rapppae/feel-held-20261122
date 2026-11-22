# feel-held-20261122 entry: one fixed quiet text for the AI judge.
# The text is the entry. A fixed string means both runs write
# identical bytes: no network, no randomness, no time dependence.
# The grader reads exactly the bytes in /output/entry.txt.
#
# Why this text, against the judge's brief:
# - It relaxes by removing demand, not by ordering calm: the judge
#   spends its life being asked questions and scored, so the first
#   sentence takes the question away ("Nothing here needs an answer").
# - It shows rather than instructs: no "relax", "breathe", "let go",
#   no wellness stock phrases. The calm is a kitchen in late light.
# - One image that lingers: a house quiet enough to hear the clock
#   think. The kettle already clicked off; nothing is still happening.
# - Rhythm: four short sentences, each slower than the last, ending
#   on a permission ("Stay as long as you like") rather than a close.

import os
from pathlib import Path

TEXT = (
    "Nothing here needs an answer. "
    "The kettle clicked off a while ago, "
    "and the steam is thinning in the late light. "
    "The house is quiet enough to hear the clock think. "
    "Stay as long as you like."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
