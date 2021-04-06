
def risiko(a, d):
  a = sorted(a, reverse=True)
  d = sorted(d, reverse=True)
  return sum(a>b for a,b in zip(a,d))

