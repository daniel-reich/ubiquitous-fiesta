
def minesweeper(grid):
  question = []
  bomb = []
  for i, c in enumerate(grid):
    for j, d in enumerate(grid[i]):
      if d == "?":
        question.append((i, j))
      elif d == "#":
        bomb.append((i, j))
  for x, y in question:
    count = 0
    for g, h in bomb:
      if ((x - 1) <= g <= (x + 1)) and ((y - 1) <= h <= (y + 1)):
        count += 1
    grid[x][y] = str(count)
  return grid

