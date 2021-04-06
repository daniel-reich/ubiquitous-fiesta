
def paths(x, y):
  return paths(x, y - 1) + paths(x - 1, y) if (x and y) else 1

