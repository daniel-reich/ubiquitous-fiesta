
def node_type(_N, _P, n):
  if n in _N:
    if n in _P:
      if _P[_N.index(n)] in _N:
        return "Inner"
      else:
        return "Root"
    else:
      return "Leaf"
  else:
    return "Not exist"

