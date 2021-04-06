
def boxes(weights):
  boxes = 0
  while True:
    current = 0
    if sum(weights) <= 10:
      return boxes + 1
    while True:
      if current + weights[0] > 10:
        boxes += 1
        break
      elif current + weights[0] == 10:
        boxes += 1
        weights.pop(0)
        break
      else:
        current += weights[0]
        weights.pop(0)

