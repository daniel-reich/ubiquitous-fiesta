
def boxes(weights):
  s = n = 0
  while weights != []:
    w = weights.pop()
    if s + w > 10:
      n += 1
      s = 0
    s += w
  return 1 + n

