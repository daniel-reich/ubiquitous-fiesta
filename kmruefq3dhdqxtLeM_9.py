
def sum_digits(a, b):
  return sum(sum(int(x) for x in str(n)) for n in range(a, b+1))

