
def node_type(_N, _P, n):
  if not n in _N: return "Not exist"
  if not n in _P: return "Leaf"
  if _P[_N.index(n)] == -1: return "Root"
  return "Inner"

