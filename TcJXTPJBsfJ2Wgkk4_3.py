
def paths(n):
  if n == 1:
    return 1
  return n * paths(n-1)

