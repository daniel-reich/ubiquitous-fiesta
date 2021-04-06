
def boxes(weights):
  weights.append(11)
  box, current_weight = 0, 0
  for idx in range(len(weights)):
    current_weight += weights[idx]
    if current_weight > 10:
      current_weight = weights[idx]
      box += 1
  return box

