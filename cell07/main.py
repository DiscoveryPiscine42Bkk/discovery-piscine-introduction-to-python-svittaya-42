# main.py

from checkmate import checkmate

def main():
    board = """\
......
..B...
......
....K.
......
......"""
    checkmate(board)

    print("---")


if __name__ == "__main__":
    main()
