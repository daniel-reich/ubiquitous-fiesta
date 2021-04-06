
def combinations(k, n):
  a = 1
  b = 1
  for l in range(n-k+1, n+1):
    a *= l
  for m in range(1, k+1):
    b *= m
  return a//b

