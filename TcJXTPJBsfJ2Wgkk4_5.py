
def paths(n):
  return n * paths(n - 1) if n > 1 else 1

