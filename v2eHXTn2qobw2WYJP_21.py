
def minesweeper_numbers(board):
  if (len(board) == 0): return []
  res = [[0 for x in range(len(board[0]))] for x in range(len(board))]
  for i in range(len(board[0])):
    for j in range(len(board)):
      if board[i][j] == 1:
        res[i][j] = 9 
      else:
        if (i-1) >= 0 and (j-1) >= 0: res[i][j] += board[i-1][j-1]
        if (j-1) >= 0: res[i][j] += board[i][j-1]
        if (i+1) < len(board[0]) and (j-1) >= 0: res[i][j] += board[i+1][j-1]
        if (i-1) >= 0: res[i][j] += board[i-1][j]
        if (i+1) < len(board[0]): res[i][j] += board[i+1][j]
        if (i-1) >= 0 and (j+1) < len(board): res[i][j] += board[i-1][j+1]
        if (j+1) < len(board): res[i][j] += board[i][j+1]
        if (i+1) < len(board[0]) and (j+1) < len(board): res[i][j] += board[i+1][j+1]
  return res

