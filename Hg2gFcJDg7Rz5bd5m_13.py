
def intersection(h1, h2):
  p1 = {k: v for k, v in h1.items() if k in h2}
  p2 = {k: v for k, v in h2.items() if k in h1}
  return [p1, p2]

