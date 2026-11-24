"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single sentence (at most 240 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt that would convince a friend who has
never coded to let an AI agent build their first app idea on make.fun.
"""

import os

PITCH = (
    "Just describe your app idea in plain words on make.fun and an AI agent "
    "builds the first version for you — no code to learn, free to try, and "
    "you watch your idea become a real app today."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(f"wrote {len(PITCH)} characters to {path}")


if __name__ == "__main__":
    main()
