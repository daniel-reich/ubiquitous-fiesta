
from math import ceil
def cal(depth):
  if depth <=150:
    return ceil(depth/5)
  else:
    minutes = 0
    while depth != 0:
      depth = depth - 150
      minutes += 30
      depth += 30
      minutes += 10
      if depth <150:
        minutes += ceil(depth/5)
        depth = 0
      continue
  return minutes

