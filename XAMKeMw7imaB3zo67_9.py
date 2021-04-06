
def trace_word_path(word, grid):
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      a=path(word, grid,[(i,j)])
      if a: return a
  return 'Not present'
​
def path(w,g,pth=[(0,0)],dir=(0,0)):
  mx,my=len(g),len(g[0])
  if len(pth)==len(w): return pth
  x,y=map(sum,zip(pth[-1],dir))
  nxt=[[(x,y)],[]][dir==(0,0)]
  if 0<=x<mx and 0<=y<my and g[x][y]==w[len(pth)-1*(nxt==[])]and not(x,y)in pth[:-1]:
    return (path(w,g,pth+nxt,(0,1)) or path(w,g,pth+nxt,(1,0)) or 
            path(w,g,pth+nxt,(0,-1)) or path(w,g,pth+nxt,(-1,0)))

