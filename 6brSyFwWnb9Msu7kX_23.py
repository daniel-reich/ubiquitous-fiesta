
def pos_neg_sort(x):
  neg = [a for a in x if a<0]
  pos = [a for a in x if a>0]
  pos.sort()
  negidx = []
  c=-1
  for a in x:
    c+=1
    if a<0:
      negidx.append(c)
  for a, b in zip(neg,negidx):
    pos.insert(b,a)
  return pos

