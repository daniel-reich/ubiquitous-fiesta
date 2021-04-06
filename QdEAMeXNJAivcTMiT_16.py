
def boxes(weights):
  box_weight = 0
  box_count = 0
  for i in weights:
    if box_weight + i <= 10:
      box_weight += i
    else:
      box_count += 1
      box_weight = i
  box_count += 1
  return box_count

