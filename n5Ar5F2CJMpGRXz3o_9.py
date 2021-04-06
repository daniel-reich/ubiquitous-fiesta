
def mineral_formation(cave):
  if sum(cave[0]) == 0:
    return 'stalagmites'
  elif sum(cave[-1]) == 0:
    return 'stalactites'
  else:
    return 'both'

