
def bingo_check(board):
  return ['x']*5 in board + [list(z) for z in zip(*board)] + \
        [[board[i][i] for i in range(5)], [board[i][4-i] for i in range(5)]]

