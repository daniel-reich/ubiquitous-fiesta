
def largest_island(lst):
  n = len(lst)
  m = len(lst[0])
  I = {(i,j):{(i,j)} for i in range(n) for j in range(m) if lst[i][j]}
  for i,j in I.keys(): 
    for x,y in [(1,1),(1,0),(1,-1),(0,-1)]:
      if (i+x,j+y) in I.keys(): 
        I[(i,j)] = I[(i,j)].union({(i+x,j+y)})
        I[(i+x,j+y)] = I[(i+x,j+y)].union({(i,j)})
  return max(len(I[(i,j)]) for i,j in I.keys())

