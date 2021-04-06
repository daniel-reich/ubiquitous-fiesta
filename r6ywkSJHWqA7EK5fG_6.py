
def printgrid(rows, cols):
  grid = [[0]*cols for i in range(rows)]
  current = 1
  for i in range(cols):
    for j in range(rows):
      grid[j][i] = current
      current+=1
  return grid

