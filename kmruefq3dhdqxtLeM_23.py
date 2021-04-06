
def sum_digits(a, b):
  return sum([sum([int(k) for k in str(i)]) for i in range(a, b + 1)])

