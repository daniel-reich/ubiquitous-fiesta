
def mineral_formation(cave):
  if 1 in cave[0]:
    return 'both' if 1 in cave[-1] else 'stalactites'
  return 'stalagmites'

