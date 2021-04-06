
def make_transpose(m):
  nr = len(m)
  nc = len(m[0])
  if((nr == 0) or (nc == 0)):
    return []
  arr = []
  for i in range(0,nc):
    l = []
    for j in range(0,nr):
      l.append(m[j][i])
    arr.append(l)
  return arr

