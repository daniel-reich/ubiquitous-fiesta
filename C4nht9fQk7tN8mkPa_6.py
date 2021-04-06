
import itertools
def cannot_capture(board):
  moves = list(itertools.product([1,-1],[2,-2])) + list(itertools.product([2,-2],[1,-1]))
  
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        for move in moves:
          if (0 <= i + move[0] <= len(board)-1) and (0 <= j + move[1] <= len(board[i])-1):
            if board[i+move[0]][j+move[1]] == 1:
              return False
  return True

