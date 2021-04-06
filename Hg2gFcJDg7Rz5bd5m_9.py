
def intersection(h1, h2):
  s = set(h1.keys() & h2.keys())
  return [{k:h1[k] for k in s},{k:h2[k] for k in s}]

