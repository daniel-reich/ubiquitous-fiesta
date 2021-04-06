
def risiko(a, d):
  a = sorted(a, reverse=True)
  d = sorted(d, reverse=True)
  lst = [i>j for i, j in zip(a, d)]
  return lst.count(True)

