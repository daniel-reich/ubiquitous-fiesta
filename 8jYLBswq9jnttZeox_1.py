
def langtons_ant(grid, column, row, n, direction=0):
  for i in range(n):
    if grid[row][column] == 1:
      direction = (direction + 1) % 4
      grid[row][column] = 0
      column, row, grid = where_to_move(grid, column, row, direction)
    else:
      direction = (direction - 1) % 4
      grid[row][column] = 1
      column, row, grid = where_to_move(grid, column, row, direction)
  return grid
​
def where_to_move(grid, column, row, direction):
  if direction % 2 == 0:
    row -= 1 - direction
  else:
    column += 2 - direction
  if row < 0:
    grid = [[0] * len(grid[0])] + grid
    row = 0
  elif row == len(grid):
    grid = grid + [[0] * len(grid[0])]
  if column < 0:
    grid = [[0] + l for l in grid]
    column = 0
  elif column == len(grid[0]):
    grid = [l + [0] for l in grid]
  return column, row, grid

