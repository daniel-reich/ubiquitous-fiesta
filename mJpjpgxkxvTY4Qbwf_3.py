
def bingo_check(board):
    rows = board
    cols = list(zip(*board))
    diag1 = [[board[x][x] for x in range(5)]]
    diag2 = [[board[x][-x-1] for x in range(5)]]
    check = rows + cols + diag1 + diag2
    return any(len(set(x))==1 and set(x)=={'x'} for x in check)

