
def third_most_expensive(dct):
  if len(dct) > 2:
    return sorted(dct, key=dct.get)[-3]
  return False

