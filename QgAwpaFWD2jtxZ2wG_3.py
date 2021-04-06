
def sum_digits(n):
  if abs(n) < 10:
    return 1
  return sum_digits(n / 10) + 1

