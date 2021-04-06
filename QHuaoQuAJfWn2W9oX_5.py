
def check_board(col, row):
  columns = 'abcdefgh'
  col = columns.index(col)
  row = abs(8-row)
​
  board = []
  for x in range(8):
    board.append([0]*8)
  
  i = 0
​
  while i < 8:
    board[row][i] = 1
    board[i][col] = 1
​
    if col-i >= 0:
      if row-i >= 0:
        board[row-i][col-i] = 1
      if row+i < 8:
        board[row+i][col-i] = 1
    
    if col+i < 8:
      if row-i >= 0:
        board[row-i][col+i] = 1
      if row+i < 8:
        board[row+i][col+i] = 1
    i += 1
  
  board[row][col] = 0
  
  return board

