
def combinations(*items):
  product = 1
  for item in items:
    if item:
      product *= item 
  return product

