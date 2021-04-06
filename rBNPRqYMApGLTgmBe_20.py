
def combinations(k, n):
  a = 1
  b = 1
  c = 1
  for i in range(1, n+1):
    a *= i
  for j in range(1, k+1):
    b *= j
  for k in range(1, n-k+1):
    c *= k
  return (a//b)//c

