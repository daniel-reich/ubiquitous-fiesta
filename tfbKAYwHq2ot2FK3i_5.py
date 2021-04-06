
# Based off of sequence A036918 in the OEIS.
from math import floor, factorial, e
def non_repeats(n):
  return floor(e * (n - 1) * factorial(n - 1))

