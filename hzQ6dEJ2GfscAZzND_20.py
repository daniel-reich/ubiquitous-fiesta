
def factory(n):
  return lambda l: list(map(lambda x: x / n, l))

