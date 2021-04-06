
def legendre(p, n):
  r = 0; i = 1
  while p**i <= n:
    r += n//(p**i)
    i += 1
  return r

