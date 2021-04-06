
def sum_digits(n):
  x = 1
  while abs(n) > 9:
    n //= 10
    x += 1
  return x

