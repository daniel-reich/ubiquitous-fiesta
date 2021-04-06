
def total_points(g, w):
  r, wd, xd = [], dict(), dict()
  for x in g:
    if all(c in w for c in x):
      wd = {k: w.count(k) for k in set(w)}
      xd = {k: x.count(k) for k in set(x)}
      if all(xd[k] <= wd[k] for k in set(x)): r += [len(x)]
  return sum([[0, 0, 0, 1, 2, 3, 54][i] for i in r])

