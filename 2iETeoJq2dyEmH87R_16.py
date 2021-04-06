
def count_digits(n, d):
  return sum(str(i).count(str(d)) for i in [i*i for i in range(n+1)])

