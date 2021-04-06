
def mineral_formation(cave):
  if cave[0].count(1) >= 1:
    if cave[len(cave) - 1].count(1) >= 1:
      return 'both'
    return 'stalactites'
  return 'stalagmites'

