
def combinations(*items):
  prod = 1
  for i in items:
    if i >0:
      prod *= i
  return prod

