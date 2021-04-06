
def get_bombs(lst, row, col, H, W):
    ans = 0
    for row2 in range(row - 1, row + 2):
        for col2 in range(col - 1, col + 2):
            if 0 <= row2 < H and 0 <= col2 < W and (row, col) != (row2, col2) and lst[row2][col2] == 1:
                ans += 1
    return ans
​
def minesweeper_numbers(board):
    if len(board) == 0:
        return board
    W, H = len(board[0]), len(board)
    ans = [[0 for _ in range(W)] for __ in range(H)]
    for row in range(H):
        for col in range(W):
            if board[row][col] == 1:
                ans[row][col] = 9
            else:
                ans[row][col] = get_bombs(board, row, col, H, W)
    return ans

