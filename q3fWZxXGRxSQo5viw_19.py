
import math
def cal(depth):
  if depth<=150:
      return math.ceil(depth/5)
  elif depth>150 and depth<300:
      tm= 40
      depth = depth-120
      return tm + math.ceil(depth/5)
  else:
      tm=80
      depth = depth-240
      return tm + math.ceil(depth/5)

