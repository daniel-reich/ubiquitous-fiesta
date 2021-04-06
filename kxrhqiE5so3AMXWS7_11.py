
import math
def get_number_of_apples(n, p):
  if n == 0 or p == "100%":
    return "The children didn't get any apples"
  p = (int(p.replace("%", ""))) * .01
  return math.floor(n - (n * p))

