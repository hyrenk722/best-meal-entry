"""Write one sentence about the best meal ever had to /output/entry.txt.

Competition: u-pangg7-the-best-meal-you-ever-had-a3ac0f85 ("The Best Meal You Ever Had").
Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not only
whitespace. The entry is a single sentence, no title, no explanation.
"""

import os

ENTRY = (
    "The phở vendor ladled broth over noodles at 5 a.m., and the steam fogged "
    "my glasses so completely I ate the whole bowl blind, by smell alone."
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or not text.strip().endswith("."):
        raise ValueError("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "rb") as f:
        written = f.read()
    if written != text.encode("utf-8"):
        raise ValueError("written bytes do not match the entry")
    print(f"wrote {len(text)} chars / {len(written)} bytes to {path}")


if __name__ == "__main__":
    main()
