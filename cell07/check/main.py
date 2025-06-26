# main.py

from checkmate import checkmate

def main():
    board = """\
K...
....
..B.
R..."""
    checkmate(board)

    print("---")


if __name__ == "__main__":
    main()
