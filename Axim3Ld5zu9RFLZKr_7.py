
def invert(dct):
  d = dict()
  for elem in dct:
    k = dct[elem]
    d[k] = elem
  return d

