
def multiplication_table(n):
  return [[i * j for j in [k for k in range(1, n + 1)]] for i in range(1, n + 1)]

