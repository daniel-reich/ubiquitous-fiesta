
def boxes(weights):
  boxes = 1
  act_weight = 0
  for weight in weights:
    act_weight += weight
    if act_weight>10:
      boxes += 1
      act_weight = weight
  return boxes

