
def mineral_formation(cave):
  if max(cave[0]) == 1 and max(cave[-1]) == 1:
    return "both"
  elif max(cave[0]) == 1:
    return "stalactites"
  elif max(cave[-1]) == 1:
    return "stalagmites"

