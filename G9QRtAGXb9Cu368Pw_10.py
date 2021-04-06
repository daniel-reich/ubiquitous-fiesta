
def combinations(*args):
  total = 1
  for item in args:
    if item == 0:
      continue
    total *= item
  return total

