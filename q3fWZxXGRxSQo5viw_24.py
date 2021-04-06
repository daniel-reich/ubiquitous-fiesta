
import math
def cal(depth):
  if depth/5/30 == 1:
    return math.ceil(depth/5)
  return math.ceil(depth/5 + depth//5//30*16)

