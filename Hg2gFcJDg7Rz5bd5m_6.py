
def intersection(h1, h2):
  isec = set(h1) & set(h2)
  return [{i:dct[i] for i in isec} for dct in (h1,h2)]

