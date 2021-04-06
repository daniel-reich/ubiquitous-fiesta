
def pd(n):
  if n==1:
    return [{1:1}]
  p=[{n:1}]
  for x in pd(n-1):
    if 1 not in x:
      z=x.copy()
      z[1]=1
      if z not in p:
        p.append(z)
    else:
      z=x.copy()
      z[1]=z[1]+1
      if z not in p:
        p.append(z)
    for y in x:
      z=x.copy()
      if x[y]==1:
        del z[y]
        z[y+1]=1 if y+1 not in z else z[y+1]+1
      else:
        z[y]=z[y]-1
        z[y+1]=1 if y+1 not in z else z[y+1]+1
      if z not in p:
        p.append(z)
  return p
def partitions(n):
  if n==0:
    return 1
  return len(pd(n))

