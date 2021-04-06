
def combinations(*items):
  c=1
  for i in items:
    c*=i if i!=0 else 1
  return c

