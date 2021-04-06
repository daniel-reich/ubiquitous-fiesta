
def bomb(lst):
  r = range(51)
  for i in r:
    for j in r:
      if all(round(dist((i,j),(x,y)) - t*.343, 1) == 0 for x,y,t in lst):
        return (i,j)
  
def dist(A,B):
  return sum((a-b)**2 for a,b in zip(A,B))**.5

