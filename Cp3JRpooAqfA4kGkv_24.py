
def node_type(_N, _P, n):
  if n in _P:
    if _N.index(n) == _P.index(-1):
      return "Root"
    return "Inner"
  if n in _N:
    return "Leaf"
  return "Not exist"

