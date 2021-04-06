
import math
​
def num_of_digits(num):
  if num > 0:
    return int(math.log10(num)) + 1
  if num == 0:
    return 1
  else:
    return int(math.log10(-1 * num)) + 1

