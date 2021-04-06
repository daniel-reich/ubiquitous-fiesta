
def hex_distance(grid):
  diag = len(grid)
  side = diag//2+1
  grid = ["".join(i.split()) for i in grid]
  grid = grid[:side] + [i.rjust(diag) for i in grid[side:]]
  (x1, y1), (x2, y2) = [
    (x, y) for y,row in enumerate(grid) for x,i in enumerate(row) if i=="x"
  ]
  dx = x2 - x1
  dy = y2 - y1
  return max(dx,dy) if dx >=0 else dy-dx

