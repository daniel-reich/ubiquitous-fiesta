
def node_type(_N, _P, n):
  if n not in _N:
    return "Not exist"
  root = _N.pop(_P.index(-1))
  if n == root:
    return "Root"
  if n not in _P:
    return "Leaf"
  return "Inner"

