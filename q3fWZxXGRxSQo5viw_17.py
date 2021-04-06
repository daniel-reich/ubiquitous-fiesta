
def cal(depth):
  import math
  a = 0
  while True:
    if depth > 150:
      a += 40
      depth -= 120
      continue
    else:
      a += math.ceil(depth / 5)
      break
  return a

