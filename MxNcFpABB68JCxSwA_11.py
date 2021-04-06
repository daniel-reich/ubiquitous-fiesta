
def legendre(p, n):
  i, res = 1, 0
  while p**i <= n:
    res += n // p**i
    i += 1
  return res

