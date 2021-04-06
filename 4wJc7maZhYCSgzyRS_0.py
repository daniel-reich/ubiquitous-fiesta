
def two_product(r, n):
  for x in r:
    if not n % x and n//x in r and r.index(x) > r.index(n//x):
      return [n//x, x]
  return None

