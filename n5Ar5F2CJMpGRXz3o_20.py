
def mineral_formation(cave):
  stalactite = 0
  stalagmite = 0
  for el in cave[0]:
    if el == 1:
      stalactite = 1
      break
  for el in cave[-1]:
    if el == 1:
      stalagmite = 1
      break
  if (stalactite == 1 and stalagmite == 1):
    return "both"
  elif stalactite == 1:
    return "stalactites"
  else:
    return "stalagmites"

