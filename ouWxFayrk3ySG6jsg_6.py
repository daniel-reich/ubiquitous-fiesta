
def who_won(board):
  if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
      return 'X'
  if board[1][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
      return 'X' 
  if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
      return 'X'
  if board[0][1] == 'X':
    if board[1][1] == 'X' and board[2][1] == 'X':
      return 'X'
    else:
      return 'O'
  elif board[0][0] == 'X':
    if board[1][1] == 'X' and board[2][2]=='X'or board[1][0] == 'X' and board[2][0] == 'X':
      return 'X'
    else:
      return 'O'
  elif board[0][2] == 'X':
    if board[1][1] == 'X' and board[2][0]=='X'or board[1][2]=='X' and board[2][2] == 'X':
      return 'X'
    else:
      return 'O'

