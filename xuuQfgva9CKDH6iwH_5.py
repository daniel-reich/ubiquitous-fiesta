
def simulate_grass(g, x, y):
  if g[x][y] == 'x': return g
  grid = [list(l) for l in g]
  n,m = len(grid),len(grid[0])
  
  stack = [(x,y)]
  grid[x][y] = '+'
  while stack:
    x,y = stack.pop()
    for z,w in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
      if 0<=z<n and 0<=w<m and grid[z][w]=='o':
        grid[z][w] = '+'
        stack.append((z,w))
  return [''.join(l) for l in grid]

