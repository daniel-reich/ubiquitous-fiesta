
def check_board(col, row):
​
    board = [[0]*8 for _ in range(8)]
    col = 'abcdefgh'.index(col)
    row = 8 - row
​
    for dx,dy in ((0,1),(1,0),(1,1),(1,-1)):
        for scalar in range(-8,8):
            if scalar:
                c = col + dx * scalar
                r = row + dy * scalar
                if 0 <= c < 8 and 0 <= r < 8:
                    board[r][c] = 1
​
    return board

