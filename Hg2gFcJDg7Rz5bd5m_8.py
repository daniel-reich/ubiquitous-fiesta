
def intersection(h1, h2):
  return [{x: h1[x] for x in h1 if x in h2.keys()}] + [{x: h2[x] for x in h1 if x in h2.keys()}]

