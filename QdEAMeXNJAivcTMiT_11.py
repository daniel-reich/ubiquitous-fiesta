
def boxes(weights):
  b=0
  c=0
  for w in weights:
    if c+w>10:
      b += 1
      c = w
    else: c+= w
  return b+1

