
def check_board(col, row):
  col = ord(col)-97
  row = 8-row
  board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
  for i in range(8):
    if i != row:
      board[i][col] = 1
  for i in range(8):
    if i != col:
      board[row][i] = 1
  for i in range(8):
    if i != col:
      temp = abs(i - col)
      if row+temp <= 7 :
        board[row+temp][i] = 1
      if row - temp >= 0:
        board[row-temp][i] = 1
  return board

