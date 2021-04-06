
import math
​
def is_sastry(n):
​
  n = int(str(n) + str(n + 1)) ** 0.5
  return n - math.floor(n) == 0

