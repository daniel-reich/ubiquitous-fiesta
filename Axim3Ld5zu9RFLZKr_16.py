
def invert(dct):
  empty = {}
  for keys, values in dct.items(): empty[values] = keys 
  return empty

