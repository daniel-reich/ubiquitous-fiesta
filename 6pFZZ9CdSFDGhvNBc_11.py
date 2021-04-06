
import math
def factor_group(num):
  check = math.sqrt(num)
  if num == int(check+.5)**2:
    return 'odd'
  else:
    return 'even'

