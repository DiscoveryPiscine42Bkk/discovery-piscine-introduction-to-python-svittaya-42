# checkmate.py

def checkmate(board_string):
    board_lines = board_string.strip().split('\n')
    size = len(board_lines)

    if any(len(line) != size for line in board_lines):
        print("Error")
        return

    board = [list(line) for line in board_lines]

    # Find the King's position
    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        print("Error")
        return

    kx, ky = king_pos

    pawn_dirs = [(-1, -1), (-1, 1)]
    bishop_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    rook_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queen_dirs = bishop_dirs + rook_dirs

    def in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    for dx, dy in pawn_dirs:
        x, y = kx + dx, ky + dy
        if in_bounds(x, y) and board[x][y] == 'P':
            print("Success")
            return

    for dx, dy in bishop_dirs:
        x, y = kx + dx, ky + dy
        while in_bounds(x, y):
            cell = board[x][y]
            if cell == 'B' or cell == 'Q':
                print("Success")
                return
            elif cell != '.':
                break
            x += dx
            y += dy

    for dx, dy in rook_dirs:
        x, y = kx + dx, ky + dy
        while in_bounds(x, y):
            cell = board[x][y]
            if cell == 'R' or cell == 'Q':
                print("Success")
                return
            elif cell != '.':
                break
            x += dx
            y += dy

    print("Fail")
