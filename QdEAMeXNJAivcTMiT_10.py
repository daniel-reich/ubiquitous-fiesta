
def boxes(weights):
  box, count = 0, 0
  for n in weights:
    count += n
    if count > 10:
      box += 1
      count = n
  return box +1

