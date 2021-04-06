
def multiplication_table(n: int) -> list:
  return [list(range(i, i * n + 1, i)) for i in range(1, n + 1)]

