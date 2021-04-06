
import math
​
def sum_digits(n):
  try:
      return round(math.log(n, 10) + 1)
  except: 
    return 1

