
def boxes(weights):
  for i in range(len(weights)):
    if i == 0:
      total = 0
      count = 0
    if total + weights[i] > 10:
      total = weights[i]
      count += 1
    else:
      total += weights[i]
    if i == len(weights) - 1:
      count += 1
  return count

