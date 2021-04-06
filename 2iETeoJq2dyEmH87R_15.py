
def count_digits(n, d):
  return "".join(str(x**2) for x in range(n+1)).count(str(d))

