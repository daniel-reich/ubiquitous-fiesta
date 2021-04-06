
def pricey_prod(d):
  return [k for k,v in sorted(d.items(), key = lambda x: x[1], reverse=True) if v >= 500]

