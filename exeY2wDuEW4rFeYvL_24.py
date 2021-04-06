
def ordered_matrix(a, b):
  k = []
  r = []
  d = []
  i = 1
  while a > 0:
    c = b
    while c > 0:
      r.append(i)
      i +=  1
      c -= 1
    d = r.copy()
    r.clear()
    k.append(d)
    a -= 1
  return k

