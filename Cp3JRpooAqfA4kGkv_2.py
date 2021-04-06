
def node_type(_N, _P, n):
  if (n,-1) in zip(_N,_P): return "Root"
  if n in _N and n in _P: return "Inner"
  if n in _N: return "Leaf"
  return "Not exist"

