
def sum_sur(x,y, G):
  B=[]
  for k in range(len(G)):
    for l in range(len(G[0])):
      if abs(x-k)<2 and abs(y-l)<2:
        B.append(G[k][l])
  return B      
  
def spotlight_map(grid):
  if grid==[[]]:
    return [[]]
  elif grid==[]:
    return []
  else:
    m=len(grid)
    n=len(grid[0])
    C=[]
    for i in range(m):
      for j in range(n):
        C.append(sum(sum_sur(i,j, grid)))
    return [C[i:i+n] for i in range(0,len(C),n)]

