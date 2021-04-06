
def combinations(*items):
  out = 1
  for i in items:
    if i != 0:
      out *= i
  return out

