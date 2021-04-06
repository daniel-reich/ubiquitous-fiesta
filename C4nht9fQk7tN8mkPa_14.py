
def cannot_capture(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 1:
        for k in [[1,2], [1,-2], [-1,2], [-1,-2], [2,1], [-2,1], [2, -1], [-2, -1]]:
          if (i+k[0] <=7 and i+k[0] >=0) and (j+k[1] <=7 and j+k[1] >=0):
            if board[i+k[0]][j+k[1]] == 1: return False
  return True

