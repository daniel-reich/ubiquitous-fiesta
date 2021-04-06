
import itertools
def game_of_life(board):
  neighbors = list(itertools.product([0,1,-1],repeat=2))[1:]
  res = [['_' for i in row] for row in board]
​
  for i in range(len(board)):
    for j in range(len(board[i])):
      n = 0
      for r, c in neighbors:
        if 0 <= i+r < len(board) and 0 <= j+c < len(board[i]):
          if board[i+r][j+c] == 1:
            n += 1
      if board[i][j] == 1:
        if n == 2 or n == 3:
          res[i][j] = 'I'
      else:
        if n == 3:
          res[i][j] = 'I'
  
  return '\n'.join([''.join(row) for row in res])

