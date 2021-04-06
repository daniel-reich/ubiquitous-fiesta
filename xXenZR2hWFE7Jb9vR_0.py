
def is_isomorphic(s, t):
  return all(s.index(x) == t.index(y) for x,y in zip(s,t))

