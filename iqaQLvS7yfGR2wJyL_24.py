
def num_of_digits(num):
  return next(i for i in range(1, 100) if abs(num) < 10**i)

