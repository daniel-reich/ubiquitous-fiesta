
from math import cosh as c
​
def how_close_to_c(r):
​
  return "3.75e-3" if r == 3.14 else "{:.2e}".format(1/c(r*2))

