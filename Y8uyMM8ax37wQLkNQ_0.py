
def matrix(n):
  base = [[0]*n for _ in range(n)]
  dirs = [[0,1],[1,0],[0,-1],[-1,0]]
  x,y = 0,-1
  k = 0
  a,b = dirs[k]
  for i in range(1,n**2+1):
    if x+a>=n or y+b>=n or base[x+a][y+b]!=0:
      k+=1
      a,b = dirs[k%4]
    base[x+a][y+b] = i
    x+= a
    y+= b
  return base

