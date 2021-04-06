
import math
def is_symmetrical(num):
  num = str(num)
  for x in range(0, math.floor(len(num)/2)):
    if num[x] != num[-1-x]:
      return False
  return True

