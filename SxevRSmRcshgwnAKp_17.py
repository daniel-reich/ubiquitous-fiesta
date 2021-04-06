
def pricey_prod(d):
  d = dict(filter(lambda x: x[1] >= 500, d.items()))
  ans = sorted(d, key=d.get, reverse=True)
  return ans

