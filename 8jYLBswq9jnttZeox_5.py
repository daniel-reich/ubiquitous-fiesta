
class Coord:
  def __init__(self, x, y):
    self.x, self.y = x, y
  def __add__(self, other):
    return Coord(self.x + other.x, self.y + other.y)
    
def extend_grid(pos, grid):
  w, h = len(grid[0]), len(grid)
  if pos.y >= h:
    grid.append([0 for _ in range(w)])
  elif pos.x >= w:
    for row in grid:
      row.append(0)
  elif pos.y < 0:
    pos.y = 0
    grid.insert(0, [0 for _ in range(w)])
  elif pos.x < 0:
    pos.x = 0
    for row in grid:
      row.insert(0, 0)
      
directions = (Coord(0, -1), Coord(1, 0), Coord(0,1), Coord(-1, 0))
def langtons_ant(grid, column, row, n, dir_idx=0):
  p = Coord(column, row)
  for _ in range(n):
    dir_idx = (dir_idx + 1) % 4 if grid[p.y][p.x] else (dir_idx - 1) % 4
    grid[p.y][p.x] = int(not grid[p.y][p.x])
    p = p + directions[dir_idx]
    extend_grid(p, grid)
  return grid

