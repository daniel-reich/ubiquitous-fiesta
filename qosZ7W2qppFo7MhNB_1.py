
def hex_distance(grid):
  m,n = len(grid),len(grid[0])
  (a,b),(c,d) = [(i,j) for i in range(m) for j in range(n) if grid[i][j]=="x"]
  vd = abs(a-c) #vertical distance
  return vd + max(d-b-vd,b-vd-d,0)//2

