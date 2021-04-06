
def multiplication_table(n):
  return [[c + c * r for c in range(1, n + 1)] for r in range(n)]

