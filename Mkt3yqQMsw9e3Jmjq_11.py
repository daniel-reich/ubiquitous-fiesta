
def disjoint_cycle_form(perm):
  d=dict([(i,x) for i , x in enumerate(perm)])
  A=[]
  for x in range(len(perm)):
    B=[]
    B.append(x)
    while d[x] not in B:
      B.append(d[x])
      x=d[x]
    if len(B)>1:
      if not any(''.join([str(x) for x in B]) in ''.join([str(x) for x in K*2]) for K in A):
        A.append(tuple(B))
  return set(A)

