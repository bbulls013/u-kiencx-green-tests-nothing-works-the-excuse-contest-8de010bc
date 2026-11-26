# Green Tests, Nothing Works: The Excuse Contest
# Writes one excuse line (<=140 chars) to /output/entry.txt

import os

EXCUSE = (
    "My tests are green because they test the code I meant to write. "
    "Production runs the code I actually wrote \u2014 untested and uninvited."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
