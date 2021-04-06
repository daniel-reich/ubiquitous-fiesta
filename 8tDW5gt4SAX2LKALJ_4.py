
def min_bombs_needed(grid):
  dirs = {'+':[(1,0),(-1,0),(0,1),(0,-1)], 'x':[(1,1),(1,-1),(-1,1),(-1,-1)]}
​
  n,m = len(grid), len(grid[0])
  bombs = [(i,j) for i in range(n) for j in range(m) if grid[i][j] in "+x"]
  
  chns = []  #will list sets of bombs in the same chain
  while bombs:
    (i,j) = bombs.pop()
    ch_ij = [c for c in chns if any((i+k,j+l) in c for (k,l) in dirs[grid[i][j]])]
    chns = [{(i,j)}.union(*ch_ij)] + [c for c in chns if c not in ch_ij]
  
  return len(chns)

