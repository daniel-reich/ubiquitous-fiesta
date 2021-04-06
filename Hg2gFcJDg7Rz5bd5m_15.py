
def intersection(h1, h2):
  return [{k: h1[k] for k in h1 if k in h2}, {k: h2[k] for k in h2 if k in h1}]

