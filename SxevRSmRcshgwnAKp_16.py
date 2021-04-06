
def pricey_prod(d):
  d = {k: v for k, v in d.items() if v >= 500}
  return [x[0] for x in sorted(d.items(), key=lambda x: x[1], reverse=True)]

