
def combinations(k, n):
  numer, denom = 1, 1
  for i in range(k):
      numer *= n - i
      denom *= (i+1)
  return numer//denom

