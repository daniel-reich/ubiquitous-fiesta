
import math
def get_number_of_apples(n, p):
  p = 100-int(p[:-1])
  x  = math.floor(n*(p)/100)
  return x if x else "The children didn't get any apples"

