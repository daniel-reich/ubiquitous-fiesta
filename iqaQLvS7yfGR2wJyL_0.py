
def num_of_digits(n):
  return next(i for i in range(1, 100) if abs(n) < 10**i)

