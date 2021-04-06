
def langtons_ant(grid, col, row, n, direction=0):
  for i in range(0,n):
    if grid[row][col] == 1:
      grid[row][col] = 0
      direction = (direction + 1) % 4
    else:
      grid[row][col] = 1
      direction = (direction - 1) % 4
    if direction == 0:
      if row == 0:
        grid.insert(0,len(grid[0])*[0])
      else:
        row -= 1
    elif direction == 1:
      if col == len(grid[0]) - 1:
        grid = list(map(lambda x: x + [0],grid))
      col += 1
    elif direction == 2:
      if row == len(grid)-1:
        grid.append(len(grid[0])*[0])
      row += 1
    elif col == 0:
      grid = list(map(lambda x: [0] + x,grid))
    else:
      col -= 1
  return grid

