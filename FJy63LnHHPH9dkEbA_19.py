
import math
def how_close_to_c(x):
  res = 1 / (math.cosh(2*x))
  counter = 0
  while res < 1:
      res *= 10
      counter += 1
  return "{:.3}e-{}".format(res, counter)

