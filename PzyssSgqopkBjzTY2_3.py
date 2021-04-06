
def can_exit(lst,path=[(0,0)],dir=(0,0)):
  d=[(0,1),(1,0),(0,-1),(-1,0)]
  mx,my=len(lst),len(lst[0])
  if path[-1]==(mx-1,my-1): return True
  x,y=map(sum,zip(path[-1],dir))
  if 0<=x<mx and 0<=y<my and not(lst[x][y]or(x,y)in path[:-1]):
    return any(can_exit(lst,path+[(x,y)],d[i]) for i in range(4))
  return False

