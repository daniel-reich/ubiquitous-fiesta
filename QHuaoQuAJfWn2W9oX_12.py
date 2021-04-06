
def check_board(col, row):
    col = ord(col) - 97
    row = 8 - row
​
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    # above
    for r in range(row - 1, -1, -1):
        board[r][col] = 1
    # beneath
    for r in range(row + 1, 8):
        board[r][col] = 1
    # right
    for c in range(col+1, 8):
        board[row][c] = 1
    # left
    for c in range(col-1, -1, -1):
        board[row][c] = 1
​
    # above-right
    inc = 1
    while col + inc < 8 and row - inc > -1:
        board[row-inc][col+inc] = 1
        inc += 1
    # above-left
    inc = 1
    while col - inc > -1 and row - inc > -1:
        board[row - inc][col - inc] = 1
        inc += 1
    # beneath-right
    inc = 1
    while col + inc < 8 and row + inc < 8:
        board[row + inc][col + inc] = 1
        inc += 1
    # beneath-left
    inc = 1
    while col - inc > -1 and row + inc < 8:
        board[row + inc][col - inc] = 1
        inc += 1
​
    return board

