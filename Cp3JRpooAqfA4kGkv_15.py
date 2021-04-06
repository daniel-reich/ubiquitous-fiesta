
def node_type(N, P, n):
    if n not in N:
        return 'Not exist'
    elif P[N.index(n)] == -1:
        return 'Root'
    elif n not in P:
        return 'Leaf'
    else:
        return 'Inner'

