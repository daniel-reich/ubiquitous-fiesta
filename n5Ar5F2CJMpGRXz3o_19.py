
def mineral_formation(cave):
  if 1 in cave[0] and 1 not in cave[-1]:
    return "stalactites"
  elif 1 in cave[-1] and 1 not in cave[0]:
    return "stalagmites"
  elif 1 in cave[-1] and 1 in cave[0]:
    return "both"

