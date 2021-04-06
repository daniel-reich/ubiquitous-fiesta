
def paths(n):
  if n == 0 or n == 1:
    return n
    
  return n * paths(n - 1)

