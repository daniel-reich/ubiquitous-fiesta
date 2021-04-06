
def simple_comp(x, y):
  if x and x[0] ** 2 in y:
    return y.remove(x[0] ** 2) or simple_comp(x[1:], y)
  return x == y == []

