
def sums_up(lst):
  d={}
  ml=[]
  l=[]
  for p in range(len(lst)):
    if p ==len(lst)-1:
      if lst[p]+z[e]==8:
        l.append(lst[p])
        l.append(z[e])
        l.append(len(lst)-1)
        ml.append(l)
        l=[]
        break
    z=lst[p+1:]
    for e in range(len(z)):
      if lst[p]+z[e]==8:
        l.append(lst[p])
        l.append(z[e])
        l.append(e+p)
        ml.append(l)
        l=[]
  ml.sort(key=lambda x:x[2])
  print(ml)
  for r in range(len(ml)):
    ml[r]=ml[r][0:2]
    ml[r].sort()
  d["pairs"]=ml
  return d

