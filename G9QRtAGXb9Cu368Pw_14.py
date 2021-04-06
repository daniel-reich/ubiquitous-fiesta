
def combinations(*items):
  comb = 1
  for item in items:
    if item != 0: comb *= item
  return comb

