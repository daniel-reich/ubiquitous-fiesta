
from itertools import *
def game_of_life(board):
  nrow, ncol = len(board), len(board[0])
  neighbors = {}
  for i, j in product(range(nrow), range(ncol)):
    neighbors[(i, j)] = []
    for x, y in product((-1, 0, 1), repeat=2):
      if 0<=i+x<nrow and 0<=j+y<ncol and (x,y)!=(0,0):
        neighbors[(i, j)].append((i+x, j+y))
  new_board = [list(row) for row in board]
  for (ci, cj), n in neighbors.items():
    num_alive = sum(board[ni][nj] for ni, nj in n)
    if board[ci][cj] and num_alive < 2: new_board[ci][cj] = '_'
    elif board[ci][cj] and num_alive < 4: new_board[ci][cj] = 'I'
    elif board[ci][cj] and num_alive >= 4: new_board[ci][cj] = '_'
    elif num_alive == 3: new_board[ci][cj] = 'I'
    else: new_board[ci][cj] = '_'
  return '\n'.join(''.join(row) for row in new_board)

