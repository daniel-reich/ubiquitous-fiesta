
def check_board(col, row):
  col = ord(col) - ord('a')
  row = 8 - row
  board = []
  for r in range(8):
    if r == row:
      l = [1]*8
      board.append(l)
    else:
      board.append([0]*8)
  for i in range(8):
    board[i][col] = 1
  board[row][col] = 0
  j = row
  g = col
  while j-1 >= 0 and g-1 >= 0:
    j -= 1
    g-= 1
    board[j][g] = 1
  j = row
  g = col
  while j-1 >= 0 and g+1 < 8:
    j -= 1
    g += 1
    board[j][g] = 1
  j = row
  g = col
  while j+1 < 8 and g+1 < 8:
    j += 1
    g += 1
    board[j][g] = 1
  j = row
  g = col
  while j+1 < 8 and g-1 >= 0:
    j += 1
    g -= 1
    board[j][g] = 1
  return board

