
from numpy import diag, transpose
def bingo_check(board):
  cols = [a for a in board]
  rows = [b for b in transpose(board)]
  d1, d2 = [], []
  for i in range(len(board)):
    d1.append(board[i][i])
    d2.append(board[i][len(board)-i-1])
  diags = [d1, d2]
  lines = cols + rows + diags
  return any(set(line) == {'x'} for line in lines)

