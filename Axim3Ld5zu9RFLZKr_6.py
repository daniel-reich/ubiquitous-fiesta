
def invert(dct):
  result = {}
  for i in dct.keys():
    result.update({dct[i]:i})
  return result

