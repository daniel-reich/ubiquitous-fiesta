
def cal(depth):
  import math
  if depth <=150:
    return math.ceil(depth/5)
  elif depth<=270:
    return math.ceil(40+(depth-120)/5)
  else:
    return math.ceil(80+(depth-240)/5)

