
def mineral_formation(cave):
  return {
    (1, 1): 'both',
    (1, 0): 'stalactites',
    (0, 1): 'stalagmites'
  }[1 in cave[0], 1 in cave[-1]]

