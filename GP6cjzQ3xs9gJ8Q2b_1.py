
def is_polydivisible(n):
  n = str(n)
  return all((int(n[:i]) / i).is_integer() for i in range(2, len(n)+1))

