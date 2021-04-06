
def paths(n):
  return 1 if n == 0 else n*paths(n-1)

