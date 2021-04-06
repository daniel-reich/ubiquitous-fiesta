
def bingo_check(board):
  for i in board:
    if i == ['x','x','x','x','x']:
      return True
  for i in range(5):
    if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i]:
      return True
  if board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]:
    return True
  elif board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]:
    return True
  else:
    return False

