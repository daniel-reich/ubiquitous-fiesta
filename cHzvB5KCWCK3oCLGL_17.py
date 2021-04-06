
def game_of_life(board):
  str = ""
  for j in range(len(board[0])):
    str += update_cell(board, 0, j)
  for i in range(1, len(board)):
    str += "\n"
    for j in range(len(board[0])):
      str += update_cell(board, i, j)
  return str
  
def neighbourhood(board, row, column):
  cnt = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      if (i, j) != (0, 0):
        if 0 <= row + i < len(board) and 0 <= column + j < len(board[0]):
          cnt += board[row + i][column + j]
  return cnt
  
def update_cell(board, row, column):
  nbh = neighbourhood(board, row, column)
  if board[row][column] == 1:
    if nbh == 2 or nbh == 3:
      return "I"
    else:
      return "_"
  else:
    if nbh == 3:
      return "I"
    else:
      return "_"

