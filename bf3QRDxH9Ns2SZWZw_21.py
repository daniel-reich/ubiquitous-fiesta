
def all_explode(lst):
  A=[(i,j) for i in range(len(lst)) for j in range(len(lst[0]))]
  P=[x for x in A if lst[x[0]][x[1]]=='+']
  X=[x for x in A if lst[x[0]][x[1]]=='x']
  d1={p:[] for p in P}
  for p in P:
    for a in A:
      if p!=a and (abs(p[0]-a[0])==1 and p[1]==a[1]) or (abs(p[1]-a[1])==1 and p[0]==a[0]):
        if lst[a[0]][a[1]]!='0':
          d1[p].append(a)
  d2={x:[] for x in X}
  for x in X:
    for a in A:
      if x!=a and (abs(x[0]-a[0])==1 and abs(x[1]-a[1])==1):
        if lst[a[0]][a[1]]!='0':
          d2[x].append(a)
  d1.update(d2)
  qu=[(0,0)]
  done={(0,0)}
  res=[]
  while qu:
    k=qu.pop(0)
    res.append(k)
    for x in d1[k]:
      if x not in done:
        qu.append(x)
        done.add(x)
  return len(P)+len(X)==len(res)

