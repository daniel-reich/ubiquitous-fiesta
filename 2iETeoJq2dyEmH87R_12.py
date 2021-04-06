
def count_digits(n, d):
  return sum([str(i**2).count(str(d)) for i in range(0,n+1)])

