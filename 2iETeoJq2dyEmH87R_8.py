
def count_digits(n, d):
  num_arr = list(x**2 for x in range(0,n+1))
  return str(list(x for x in num_arr)).count(str(d))

