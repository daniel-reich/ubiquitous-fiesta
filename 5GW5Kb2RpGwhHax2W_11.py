
def spiral_idx(m,n,b):
  print(m,n)
  ret=[]
  if m<=0 or n<=0:
    return []
  ret+=[[b+0,b+x] for x in range(n)]
  #print(ret)
  if n>1:
    ret+=[[b+x,b+n-1] for x in range(1,m)]
  #print(ret)
  if m>1:
    ret+=[[b+m-1,b+x] for x in range(n-2 if n>1 else 0,-1,-1)]
  #print(ret)
  ret+=[[b+x,b+0] for x in range(m-2,0,-1)]
  #print(ret)
  return ret+spiral_idx(m-2,n-2,b+1)
​
def spiral_transposition(l):
  m=len(l)
  if isinstance(l[0],list):
    n=len(l[0])
  else:
    return 'Error: input not a 2-dim list'
  idx=spiral_idx(m,n,0)
  ret=list(map(lambda x: l[x[0]][x[1]],idx))
  return ret

