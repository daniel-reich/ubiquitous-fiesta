
def safecracker(start, increments):
  l=[]
  if start>increments[0]:
    r=start-increments[0]
  else:
    r=100-increments[0]+start
    if r>100:
      r=r-100
  l.append(r) 
  g=l[0]+increments[1]
  if g>100:
    g=g-100
  l.append(g)
  if l[1]>increments[2]:
    v=l[1]-increments[2]
  else:
    v=100-increments[2]+l[1]
  l.append(v) 
  return l

