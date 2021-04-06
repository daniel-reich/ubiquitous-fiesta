
def intersection(h1, h2):
  f = lambda x, y: {k: x[k] for k in x if k in y}
  return [f(h1, h2), f(h2, h1)]

