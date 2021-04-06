
def islands_perimeter(grid):
  result = 0
  for x in range(len(grid)):
    for y in range(len(grid[0])):
      if grid[x][y]:
        result += get_area(grid, x, y)
  return result
​
def get_area(grid, x, y):
  result = 0
  if x:
    if grid[x - 1][y] == 0:
      result += 1
  else:
    result += 1
  if y:
    if grid[x][y - 1] == 0:
      result += 1
  else:
    result += 1
  if x < len(grid) - 1:
    if grid[x + 1][y] == 0:
      result += 1
  else:
    result += 1
  if y < len(grid[0]) - 1:
    if grid[x][y + 1] == 0:
      result += 1
  else:
    result += 1
  return result

