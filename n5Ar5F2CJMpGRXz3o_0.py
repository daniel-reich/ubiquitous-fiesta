
def mineral_formation(cave):
  return ['both', 'stalactites', 'stalagmites'][(1 in cave[0]) - (1 in cave[-1])]

