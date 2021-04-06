
def combinations(*items):
  res = 1
  for i in items:
    res *= i + (i == 0)
  return res

