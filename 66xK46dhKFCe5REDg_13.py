
def x_and_o(board):
  board = [row.split('|') for row in board]
  moves = [(i, j) for (i, row) in enumerate(board) for (j, val) in enumerate(row) if val == ' ']
​
  for move in moves:
    (i, j) = move
    board[i][j] = 'X'
​
    if gameOver(board):
      return [i + 1, j + 1]
      
    board[i][j] = ' '
​
  return False
​
def gameOver(board):
  if (crossedRow(board) or
  crossedCol(board) or
  crossedDiag(board)):
    return True
​
  return False
​
def crossedRow(board):
  for row in board:
    if (row[0] == 'X' and
    row[0] == row[1] and
    row[1] == row[2]):
      return True
​
  return False
​
def crossedCol(board):
  for i in range(3):
    if (board[0][i] == 'X' and
    board[0][i] == board[1][i] and
    board[1][i] == board[2][i]):
      return True
​
  return False
​
def crossedDiag(board):
  if board[1][1] == 'X':
    if (board[1][1] == board[0][0] and
    board[0][0] == board[2][2]):
      return True
​
    elif (board[1][1] == board[0][2] and
    board[0][2] == board[2][0]):
      return True
​
  return False

