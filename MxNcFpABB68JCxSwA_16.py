
def legendre(p, n):
  div = p
  s = 0
  while True:
    t = n // div
    if t == 0:
      return s
    s += t
    div *= p

