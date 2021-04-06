
import math
def shortestDistance(txt):
  nums = [int(t) for t in txt.split(',')]
  a = math.pow(nums[0] - nums[2], 2) 
  b = math.pow(nums[1] - nums[3], 2)
  return round(math.sqrt(a + b), 2)

