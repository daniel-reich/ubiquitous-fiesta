
def check_board(col, row):
  board = [[0]*8 for _ in range(8)]
  col, row = ord(col) - 97, abs(row - 8)
  
  for i in range(8):
    for j in range(8):
      if i == row or j == col or abs(row-i) == abs(col-j):
        board[i][j] = 1
  board[row][col] = 0
  return board

