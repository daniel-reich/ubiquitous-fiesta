
def mineral_formation(cave):
  top = len([i for i in cave[0] if i == 0]) == len(cave[0])
  bottom = len([i for i in cave[-1] if i ==0]) == len(cave[-1])
  return "both" if not top and not bottom else "stalagmites" if top else "stalactites"

