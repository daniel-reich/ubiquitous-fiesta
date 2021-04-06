
def intersection(h1, h2):
  return [{x: v for x, v in h1.items() if x in h2.keys()}, {x: v for x, v in h2.items() if x in h1.keys()}]

