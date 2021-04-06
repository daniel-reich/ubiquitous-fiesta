
def is_ladder_safe(ldr):
  length = [i for i in ldr if len(i) > 4]
  if len(length) != len(ldr):
      return False
  rungs = [i for i in range(len(ldr)) if ldr[i].count(" ") == 0]
  if not rungs:
    return False
  distance = rungs[1] - rungs[0]
  if distance > 3:
      return False
  broke = [i for i in ldr if i.count("#") > 2 and " " in i]
  if broke:
      return False
  for c, r in enumerate(rungs[1:], 1):
      if rungs[c-1] != r-distance:
          return False
  return True

