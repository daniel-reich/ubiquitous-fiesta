
def legendre(p, n):
  sum = 0
  i = 1
  while n // p**i >= 1:
    sum += n // p**i
    i += 1
  return sum

