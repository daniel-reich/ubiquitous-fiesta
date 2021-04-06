
def node_type(_N, _P, n):
  for i , j in zip(_N,_P):
    if i == n and j == -1:
      return 'Root'
  if n not in _N and n not in _P:
    return "Not exist"
  elif n in _N and n in _P :
    return 'Inner'
  elif n in _N and n not in _P:
    return 'Leaf'
  else:
    return 'Root'

