
def grouping(w):
  b="ACBDEFGHIJKLMNOPQRSTUVQXYZ"
  l=[]
  d={}
  q={}
  c=0
  a=[]
  for e in w:
    for r in e:
      if r in b:
        c+=1
    if c in d.keys():
      d[c]=d[c]+[e]
    else:
      d[c]=[e]
    c=0
  for k in d.keys():
    l.append(k)
  l.sort()
  for v in l:
    x=list(d[v])
    for y in range(len(x)):
      x[y]=x[y].lower()
    x.sort()
    for y in x:
      for j in d[v]:
        if j.lower()==y:
          a.append(j)
    q[v]=a
    a=[]
  return q

