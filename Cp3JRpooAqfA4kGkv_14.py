
def node_type(_N, _P, n):
  if n in _N and _P[_N.index(n)]==-1:return "Root"
  if n in _N and n in _P:return "Inner"
  if n in _N:return "Leaf"
  return "Not exist"

