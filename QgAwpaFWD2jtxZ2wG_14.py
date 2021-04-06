
def sum_digits(n):
  if n < 10:
    return 1
  return 1 + sum_digits(n//10)

