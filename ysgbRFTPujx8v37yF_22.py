
def row_sum(n):
  quad = lambda x: int(0.5 * x * x - 0.5 * x + 1)
  return sum(range(quad(n), quad(n + 1)))

