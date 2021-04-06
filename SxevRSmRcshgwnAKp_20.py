
def pricey_prod(d):
  l = sorted(d, key=d.get, reverse=True)
  return [i for i in l if d[i] >= 500]

