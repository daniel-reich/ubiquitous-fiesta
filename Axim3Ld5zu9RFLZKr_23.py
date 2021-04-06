
def invert(dct):
  ndct = {}
  for i in reversed(range(0, len(dct.values()))):
    k = list(dct.keys())
    ndct[dct[k[i]]] = k[i]
  return ndct

