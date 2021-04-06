
import math
def factor_group(num):
  if math.sqrt(num).is_integer():
    return "odd"
  else:
    return "even"

