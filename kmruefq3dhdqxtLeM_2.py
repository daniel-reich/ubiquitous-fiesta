
def sum_digits(a, b):
  digits = ''.join(str(i) for i in range(a, b + 1))
  return sum(int(i) for i in digits)

