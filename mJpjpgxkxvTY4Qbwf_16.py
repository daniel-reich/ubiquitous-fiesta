
def bingo_check(board):
  A=[list(x) for x in zip(*board)]
  B=[[board[i][i] for i in range(len(board))]]
  C=[[board[i][len(board)-i-1] for i in range(len(board))]]
  return any(x==["x"]*len(board) for x in board+A+B+C)

