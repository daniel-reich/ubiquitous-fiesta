
def is_isomorphic(s, t):
  d = dict(zip(t, s))
  return s == "".join(d[x] for x in t)

