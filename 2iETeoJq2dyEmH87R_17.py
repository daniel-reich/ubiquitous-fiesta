
def count_digits(n, d):
  res = [str(pow(i,2)) for i in range(n+1)]
  return sum([el.count(str(d)) for el in res])

