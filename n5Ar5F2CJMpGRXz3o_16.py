
def mineral_formation(cave):
  if(1 in cave[0] and 1 in cave[-1]):
    return "both";
  if(1 in cave[0]):
    return "stalactites"
  else:
    return "stalagmites"

