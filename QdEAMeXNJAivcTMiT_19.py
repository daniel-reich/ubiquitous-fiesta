
def boxes(weights):
  s = 0
  t = 1
  for i in range(len(weights)):
    if s + weights[i] > 10:
      t += 1
      s = weights[i]
    else:
      s += weights[i]
  return t

