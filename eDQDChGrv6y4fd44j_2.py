
def can_put(t,d):
  p,q = 0,0
  for i in t.split():
    if len(i) > d[1]:
      return False
    if len(i)+p > d[1]:
      p = len(i)+1
      q += 1
    else:
      p += len(i)+1
  return q < d[0]

