
from collections import deque
def num_regions(grid):
  h, w = len(grid), len(grid[0])
  
  def in_bounds(x, y):
    return (0 <= x < w) and (0 <= y < h)
  
  def bfs(x0, y0):
    queue = deque([(x0, y0)])
    while queue:
      x, y = queue.pop()    
      grid[y][x] = 0
      for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if in_bounds(nx, ny) and grid[ny][nx] != 0:
          queue.appendleft((nx, ny))
  
  count = 0
  for y in range(h):
    for x in range(w):
      if grid[y][x]:
        count += 1
        bfs(x, y)
  return count

