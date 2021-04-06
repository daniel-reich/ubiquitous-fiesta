
def harry(po):
  if not po[0]:
    return -1
  if len(po) == 1:
    return sum(po[0])
  if len(po[0]) == 1:
    return sum(list(map(lambda x: x[0],po)))
  return max(sum(po[0]) + sum(list(map(lambda x:x[-1],po[1::]))),sum(list(map(lambda x: x[0], po))) + sum(po[-1][1::]))

