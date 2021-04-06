
import math
def cal(depth):
  min = 0
  depth_left = depth
  while depth_left > 0:
    if depth_left <= 150:
      min += depth_left / 5
      depth_left = 0
    else:
      min += (30 + 10)
      depth_left -= (150 - 30)
  return  math.ceil(min)

