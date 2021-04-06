
def legendre(p, n):
  c, i = 0, 1
  while p**i <= n: 
    c += n//p**i
    i += 1
  return c

