
def pricey_prod(d):
  d2 = {k: v for (k,v) in d.items() if v >= 500}
  return sorted(d2.keys(), key=d2.get, reverse=True)

