
def mineral_formation(cave):
    a, b = cave[0], cave[-1]
    return 'both' if any(a) and any(b) else \
           'stalactites' if any(a) and not any(b) else \
           'stalagmites' if not any(a) and any(b) else 0

