
def legendre(p, n):
  
  x = 1
  res = 0
  while p**x <= n:
    res += n//(p**x)
    x += 1
  return res

