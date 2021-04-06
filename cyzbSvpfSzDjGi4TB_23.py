
def harmonic(n):
  x, c = 0, 1
  while c <= n:
    x = x + 1/c
    c += 1
  return round(x,3)

