
def mineral_formation(cave):
    for i in cave:
        if any(cave[0]) and any(cave[-1]):
            return "both"
        elif any(cave[0]):
            return "stalactites"
        elif any(cave[-1]):
            return "stalagmites"

