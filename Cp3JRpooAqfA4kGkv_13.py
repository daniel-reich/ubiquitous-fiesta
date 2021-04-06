
def node_type(_N, _P, n):
  if n in _N:
    if n not in _P:
      return "Leaf"
    if _P[_N.index(n)]==-1:
      return "Root"
    if _P[_N.index(n)]!=-1 and n in _P:
      return "Inner"
  else:
    return "Not exist"

