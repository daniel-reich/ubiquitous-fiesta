
def paths(x, y):
  if x == 0 or y == 0:
    return 1
  return paths(abs(x)-1, abs(y)) + paths(abs(x), abs(y)-1)

