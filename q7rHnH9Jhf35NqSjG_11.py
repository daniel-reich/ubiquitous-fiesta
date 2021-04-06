
def trailing_zeros(n):
  c = 0
  while (n > 5):
    n //= 5
    c += n
  return c

