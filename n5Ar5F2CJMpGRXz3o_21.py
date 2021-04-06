
def mineral_formation(cave):
    a = cave[0].count(1) >= 1
    b = cave[-1].count(1) >= 1
    return "both" if a and b else "stalagmites" if b else "stalactites"

