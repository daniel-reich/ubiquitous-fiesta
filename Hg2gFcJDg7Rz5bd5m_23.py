
def intersection(h1, h2):
  inter = sorted(set(h1.keys()) & set(h2.keys()))
  d = {}
  e = {}
  for i in inter:
    d[i] = h1[i]
    e[i] = h2[i]
  return [d, e]

