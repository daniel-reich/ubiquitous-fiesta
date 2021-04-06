
def node_type(_N, _P, n):
  all = [x for x in _N]
  if n not in all:
    return 'Not exist'
  else:
    for i in _P:
      all.append(i)
    for i in all:
      if ((i == n) and(i in _N) and(i not in _P)):
        return 'Leaf'
      if (i == n) and(_P[_N.index(i)] == -1):
        return 'Root'
      if (i == n) and(i in _P) and (i in _N) and (_P[_N.index(i)] != -1):
        return 'Inner'

