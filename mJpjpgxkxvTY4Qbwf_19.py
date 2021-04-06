
def bingo_check(board):
  for l in board + list(zip(*board)):
    if set(l) == {"x"}: return True
  return all(board[i][i] == 'x' for i in range(5)) or all(board[i][4 - i] == 'x' for i in range(5))

