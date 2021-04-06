
def intersection(h1, h2):
  return [{x: h1[x] for x in h1 if x in h2}, {y: h2[y] for y in h2 if y in h1}]

