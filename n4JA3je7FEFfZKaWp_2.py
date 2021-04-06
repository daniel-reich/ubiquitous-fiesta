
import math
def million_in_month(first_month, multiplier):
  #goal = 10**6# or 1000000;
  return math.ceil(math.log((1-1000000*(1-multiplier)/first_month),multiplier))

