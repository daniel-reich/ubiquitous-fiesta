
import math
​
def i_sqrt(n):
  if n < 0:
    return "invalid"
  else:
    count = 0
    while n >= 2:
      n = math.sqrt(n)
      count += 1
  return count

