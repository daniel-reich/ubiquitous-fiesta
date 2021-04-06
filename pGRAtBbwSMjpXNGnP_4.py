
def is_sorted(w, l):
  for (x, y) in zip(w, w[1:]):
    if x == y or y.startswith(x): continue
    if x.startswith(y): return False
    for k in range(len(x)):
      a, b = l.index(x[k]), l.index(y[k])
      if a < b: break
      if a > b: return False
  return True

