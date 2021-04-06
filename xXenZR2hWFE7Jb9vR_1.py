
def pat(w):
  return [w.index(l) for l in w]
def is_isomorphic(s, t):
  return pat(s)==pat(t)

