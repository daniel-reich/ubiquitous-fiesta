
def bingo_check(board):
  board2 = list(zip(*board))
  for i in range(5):
    if ["x", "x", "x", "x", "x"] == board[i] or ("x", "x", "x", "x", "x") == board2[i]:
      return True
  return any([all([board[i][i]=='x' for i in range(5)]), all([board[i][4-i]=='x' for i in range(5)])])

