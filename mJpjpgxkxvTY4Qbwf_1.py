
def bingo_check(board):
    return h(board) or v(board) or d(board) 
def h(board):
    return any(set(x) == {"x"} for x in board)
def v(board):
    return any(set(x) == {"x"} for x in zip(*board))
def d(board):
    one = all(board[x][x] == "x" for x in range(len(board)))
    two = all(board[x][len(board) -1 - x] == "x" for x in range(len(board)))
    return one or two

