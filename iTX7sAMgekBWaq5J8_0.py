
def add_up_to(n):
  return sum(range(1, n + 1))
  # or: return n * (n + 1) // 2
  # or: return n if n == 0 else n + addUpTo(n - 1)

