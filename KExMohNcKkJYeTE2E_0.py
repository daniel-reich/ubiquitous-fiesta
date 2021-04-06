
def is_orthogonal(A, B):
  return not sum(x*y for x, y in zip(A,B))

