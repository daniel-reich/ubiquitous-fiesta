
def _nespr(lst, product):
  for i in range(2, len(lst) + 1):
    product *= i
  for item in lst:
    if isinstance(item, list):
      product = _nespr(item, product)
  return product
  
def nespers(lst):
  return _nespr(lst, 1)

