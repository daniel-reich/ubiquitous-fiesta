
import math
​
def power_of_two(num):
  if num == 1:
      return True
  for i in range(1, num):
    if num == 2**i:
      return True
  return False

