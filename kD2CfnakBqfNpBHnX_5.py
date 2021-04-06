
def islands_perimeter(grid):
  t = 0
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j]:
        for k in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
          if not (0 <= i + k[0] < len(grid) and 0 <= j + k[1] < len(grid[0])) or not grid[i+k[0]][j+k[1]]:
            t += 1
  return t

