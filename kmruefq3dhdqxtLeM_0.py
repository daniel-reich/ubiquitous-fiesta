
def sum_digits(a, b):
  return sum(sum(map(int, str(i))) for i in range(a, b + 1))

