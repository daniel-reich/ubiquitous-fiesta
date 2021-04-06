
def paths(x, y):
  return paths(x-1, y) + paths(x, y-1) if x and y else 1

