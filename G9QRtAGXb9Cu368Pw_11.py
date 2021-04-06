
def combinations(*items):
  res = 1
  for i in items:
    if i != 0:
      res *= i
  return res

