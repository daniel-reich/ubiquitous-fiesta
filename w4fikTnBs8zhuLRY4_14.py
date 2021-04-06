
def rep_set(n):
  l = []
  for i in range(n):
    l.append(l[:])
  return l

