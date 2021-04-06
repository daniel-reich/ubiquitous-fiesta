
def paths(n):
  return n*paths(n-1) if n else 1

