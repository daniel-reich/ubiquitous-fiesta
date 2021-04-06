
def can_put(txt, dim):
  words = txt.split()
  rows_len, cols_len = dim
  board = [[" " for _ in range(cols_len)] for _ in range(rows_len)]
  row = col = 0
  while words:
    word = words.pop(0)
    if len(word) > cols_len - col:
      if col > 0:  # start from new line
          row += 1
          col = 0
      else:
        return False
    for c in word:
      try:
        board[row][col] = c
      except IndexError:
        return False
      col += 1
    col += 1  # for space
  return True

