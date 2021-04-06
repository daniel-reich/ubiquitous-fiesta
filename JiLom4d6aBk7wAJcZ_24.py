
import math
def is_sastry(n):
  num = math.sqrt(int(str(n) + str(n+1)))
  return num == math.floor(num)

