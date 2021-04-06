
def rank(lst):
  p = {}
  for i, v in enumerate(sorted(lst)):
    p.setdefault(v, []).append(i)
  return [sum(p[v])/len(p[v]) for v in lst]

