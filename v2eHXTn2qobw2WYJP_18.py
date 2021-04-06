
def minesweeper_numbers(board):
  b = board
  for x in range(0, len(b)):
    for y in range(0, len(b[x])):
      if b[x][y] == 1:
        b[x][y] = 9
  for x in range(0, len(b)):
    for y in range(0, len(b[x])):
      if b[x][y] == 0:
        bombs = 0
        for x2 in range(-1, 2):
          for y2 in range(-1, 2):
            if x + x2 >= 0 and x + x2 < len(b) and y + y2 >= 0 and y + y2 < len(b[0]) and b[x + x2][y + y2] == 9:
              bombs += 1
        b[x][y] = bombs
  return b

