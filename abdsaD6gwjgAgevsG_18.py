
from math import ceil
def power_ranger(power, minimum, maximum):
  counter = 0
  n = ceil(minimum**(1/power))
  while minimum <= n**power <= maximum:
    counter += 1
    n += 1
  return counter

