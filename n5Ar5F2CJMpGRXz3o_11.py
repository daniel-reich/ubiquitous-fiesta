
def mineral_formation(cave):
  if sum(cave[0]) > 0:
    if sum(cave[-1]) > 0:
      return 'both'
    else:
      return 'stalactites'
  else:
    return 'stalagmites'

