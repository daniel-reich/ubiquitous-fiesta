
import numpy as np
def bingo_check(board):
  bingo = False
  bingo_board = np.array(board) == "x"
  if np.max(np.sum(bingo_board, axis = 0)) == 5 or np.max(np.sum(bingo_board, axis = 1)) == 5:
    bingo = True
  if np.trace(bingo_board) == 5 or np.trace(np.flip(bingo_board,axis=1))==5:
    bingo = True
  return bingo

