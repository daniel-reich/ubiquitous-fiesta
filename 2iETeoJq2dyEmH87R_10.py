
def count_digits(n, d):
  return sum(str(x**2).count(str(d)) for x in range(n+1))

