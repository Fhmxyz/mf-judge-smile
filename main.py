import os

LINE = (
    "This morning the stray cat who has hissed at me for a whole year climbed onto "
    "my shoe, curled up, and purred through two sips of coffee before remembering "
    "she hates me."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
