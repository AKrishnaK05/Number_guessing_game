from tree import build_balanced_bst
from game import play_game


def main():
    root = build_balanced_bst(1, 100)
    play_game(root)


if __name__ == "__main__":
    main()