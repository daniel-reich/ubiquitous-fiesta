
def paths(x, y):
  res = [[1]*(y+1) for _ in range(x+1)]
  for i in range(1,x+1):
    for j in range(1,y+1):
      res[i][j] = res[i-1][j]+res[i][j-1]
  return res[-1][-1]

