
def boxes(weights):
  curr,box = 0,1
  for w in weights:
    if curr + w > 10:
      box += 1
      curr = w
    else:
      curr += w
  return box

