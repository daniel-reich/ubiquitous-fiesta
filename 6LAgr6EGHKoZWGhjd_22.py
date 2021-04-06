
def final_direction(i,l):
  d=list('NESW')
  l=list(l)
  f=d.index(i)
  for i in range(f): d.append(d.pop(0))
  while l:
    if l.pop(0)=='R': d.append(d.pop(0))
    else: d=[d.pop()]+d
  return d[0]

