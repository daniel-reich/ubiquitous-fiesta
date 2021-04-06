
def node_type(_N, _P, n):
  if n not in _N: return 'Not exist'
  if _P[_N.index(n)] < 0: return 'Root'
  if n not in _P: return 'Leaf'
  return 'Inner'

