
def node_type(N, P, n):
  if n in N:
    return 'Root' if P[N.index(n)] == -1 else 'Inner' if n in P else 'Leaf'
  return 'Not exist'

