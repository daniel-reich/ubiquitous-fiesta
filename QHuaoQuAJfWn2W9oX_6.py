
def check_board(col, row):
  r = ord(col) - ord('a')
  c = 8 - row
​
  def on_treat(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
      return True
    if abs(x1 - x2) == abs(y1 - y2):
      return True
    return False
​
  rows = [[0 for _ in range(8)] for _ in range(8)]
  for i in range(8):
    for j in range(8):
      if on_treat(i, j, c, r):
        rows[i][j] = 1
  rows[c][r] = 0
  return rows

