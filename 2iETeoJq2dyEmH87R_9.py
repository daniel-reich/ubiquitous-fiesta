
def count_digits(n, d):
  c = 0
  for i in range(n + 1): c += str(i ** 2).count(str(d))
  return c

