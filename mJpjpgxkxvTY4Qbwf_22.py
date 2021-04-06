
import numpy as np
def bingo_check(board):
  l_diag = np.diag(board)
  r_diag = np.diag(np.fliplr(board))
  rows = [all(c == 'x' for c in elem) for elem in board]
  cols = [all(c == 'x' for c in elem) for elem in zip(*board)]
  diags = [all(c == 'x' for c in elem) for elem in [l_diag] + [r_diag]]
  return any(rows) or any(cols) or any(diags)

