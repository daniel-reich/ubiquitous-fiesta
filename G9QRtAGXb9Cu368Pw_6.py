
def combinations(*items):
  r=1
  for i in items:
    if i: r*=i
  return r

