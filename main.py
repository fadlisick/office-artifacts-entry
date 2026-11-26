"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt.
Deterministic: no randomness, no network, no clock.
"""

import os

PLACARD = (
    "Desk plant, c. 2021. Plastic pot, artificial leaves. "
    "Watered faithfully for three years by a team that never "
    "noticed it was fake. Gift of Wellness."
)


def main() -> None:
    if not 1 <= len(PLACARD) <= 180:
        raise ValueError("placard must be 1 to 180 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLACARD)


if __name__ == "__main__":
    main()
