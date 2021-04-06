
def node_type(_N, _P, n):
  if n not in _N and n not in _P:
    return 'Not exist'
  if _P[_N.index(n)] == -1:
    return 'Root'
  if n in _N and n not in _P:
    return 'Leaf'
  if n in _N and n in _P:
    return 'Inner'

