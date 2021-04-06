
def boxes(weights):
  boxes = 0
  sum = 0
  for item in weights:
    sum += item
    if(sum > 10):
      boxes += 1
      sum = item
  boxes += 1
  return boxes

