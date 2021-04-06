
def node_type(_N, _P, n):
  if n not in _N:
    return "Not exist"
  
  ni = _N.index(n)
  if _P[ni] == -1:
    return "Root"
    
  if n not in _P:
    return "Leaf"
    
  return "Inner"

