
def scan(grid):
  p1 = None
  p2 = None
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j]=='x':
        if p1==None:
          p1 = [i,j]
        else:
          p2 = [i,j]
          return p1,p2
          
def hex_distance(grid):
  for g in grid: print(g)
  p1,p2 = scan(grid)
  dy = p2[0]-p1[0]
  dx = max(abs(p2[1]-p1[1])-dy,0)//2
  return dx+dy

