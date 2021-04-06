
def pricey_prod(d):
  return sorted((k for k,v in d.items() if v >= 500), key=lambda x: -d[x])

