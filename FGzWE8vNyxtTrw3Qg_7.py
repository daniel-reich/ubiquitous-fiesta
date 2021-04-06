
def num_regions(grid):
  x = len(grid)
  y = len(grid[0])
  regions = [[None for _ in range(y)] for _ in range(x)]
​
  label = 0
  queue = []
​
  def check_neighbor(i, j,v):
    if not regions[i][j] and grid[i][j] == v:
      regions[i][j] = label
      queue.insert(0, (i, j))
​
  for i in range(x):
    for j in range(y):
      if regions[i][j]:continue
      label += 1 
      regions[i][j] = label
      queue = [(i, j)]
      v = grid[i][j]
      while queue:
        (X, Y) = queue.pop()
        if X > 0:
          check_neighbor(X-1, Y,v)
        if X < x-1:
          check_neighbor(X+1, Y,v)
        if Y > 0:
          check_neighbor(X, Y-1,v)
        if Y < y-1:
          check_neighbor(X, Y+1,v)
  for i in range(x):
    for j in range(y):
      if grid[i][j]==0:
        regions[i][j]=0
  S=set(sum(regions,[]))
  return len(S)-1

