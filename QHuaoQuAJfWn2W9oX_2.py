
def check_board(col, row):
  col = ord(col) - 97
  board = []
  for r in range(8, 0, -1):
    tmp = []
    for c in range(8):
      if not (col == c and row == r) and (abs(r - row) == abs(c - col) or col == c or row == r):
        tmp.append(1)
      else:
        tmp.append(0)
    board.append(tmp)
  return board

