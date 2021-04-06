
def check_board(col, row):
    board = [[0 for c in range(8)] for r in range(8)]
    row, col = 8 - row, ord(col) - 97
    for c in range(col + 1, 8):
        board[row][c] = 1
    for c in range(col - 1, -1, -1):
        board[row][c] = 1
    for r in range(row + 1, 8):
        board[r][col] = 1
    for r in range(row - 1, -1, -1):
        board[r][col] = 1
    r, c = row + 1, col + 1
    while r < 8 and c < 8:
        board[r][c] = 1
        r += 1
        c += 1
    r, c = row - 1, col + 1
    while r >= 0 and c < 8:
        board[r][c] = 1
        r -= 1
        c += 1
    r, c = row + 1, col - 1
    while r < 8 and c >= 0:
        board[r][c] = 1
        r += 1
        c -= 1
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        board[r][c] = 1
        r -= 1
        c -= 1
    return board

