
def count_digits(n, d):
  result = [str(i**2) for i in range(0,n+1)]
  return sum([i.count(str(d)) for i in result])

