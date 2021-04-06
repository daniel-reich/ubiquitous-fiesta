
def node_type(_N, _P, n):
    if n not in _N and n not in _P:
        return 'Not exist'
    for i in range(len(_N)):
        if _N[i] == n and _P[i] == -1:
            return 'Root'
    if n in _N and n in _P:
        return 'Inner'
    return 'Leaf'

