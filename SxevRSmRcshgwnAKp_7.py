
def pricey_prod(d):
  return sorted([x for x, y in  d.items() if y >= 500], key=lambda x: d[x])[::-1]

