
def prime(x):
  x_sqr = int(x ** (1/2))
  sum = 0
  for i in range(1, x_sqr + 1):
    if x%i == 0:
      sum += 1
  return sum == 1

