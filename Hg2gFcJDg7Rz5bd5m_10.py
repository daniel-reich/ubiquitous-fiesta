
def intersection(h1, h2):
  return [{i:h1[i] for i in h1 if i in h2}, {i:h2[i] for i in h2 if i in h1}]

