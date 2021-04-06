
def can_patch(bridge, planks):
    hole = 0
    holes = []
    for i, j in enumerate(bridge):
        if j == 0:
            hole += 1
        else:
            if hole:
                holes.append(hole)
                hole = 0
​
    real = [hole for hole in holes if hole > 1]
​
    if real:
        for hole in holes:
            available = [i for i in planks if i >= hole - 1]
            if available:
                fix = min(available)
                planks.remove(fix)
            else:
                return False
​
    return True

