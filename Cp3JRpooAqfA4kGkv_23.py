
def node_type(_N, _P, n):
  if n not in _P:
    return "Leaf" if n in _N else "Not exist"
  return "Root" if _P[_N.index(n)]==-1 else "Inner"

