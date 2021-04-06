
def legendre(p, n):
  x = 1
  y = 0
  while p**x <= n:
    y = y + int(n/(p**x))
    x += 1
  return y

