
def to_list(dct):
  keys = list(dct.keys())
  keys.sort()
  return [[key, dct[key]] for key in keys]

