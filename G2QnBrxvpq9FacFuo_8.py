
def possible_path(r):
  return all(type(x) != type(y) for x, y in zip(r, r[1:]))

