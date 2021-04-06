
def count_digits(n, d):
  a = [str(i**2).count(str(d)) for i in range(n+1)]
  return sum(a)

