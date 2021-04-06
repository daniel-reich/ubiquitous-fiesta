
def count_digits(n, d):
  return ''.join(map(str, [i**2 for i in range(n+1)])).count(str(d))

