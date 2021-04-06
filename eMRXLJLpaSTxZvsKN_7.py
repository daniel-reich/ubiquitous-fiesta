
def is_ladder_safe(ldr):
    if len([len(i) for i in ldr if len(i) >= 5]) ==  len(ldr):
        bar = '#' + (len(ldr[0])-2)*" " + "#"
        grip = "#" * len(ldr[0])
        space, slst = 0, []
        if any([bar!=ldr[0],bar!=ldr[-1],grip!=ldr[1],grip!=ldr[-2]]):
            return False
        ldr = ldr[2:-1]
        for i in ldr:
            if space < 3:
                if i == bar:
                    space += 1
                elif i == grip:
                    slst.append(space)
                    space = 0
                else:
                    return False
            else:
                return False
        sample = slst[0]
        for i in slst:
            if i != sample:
                return False
        return True
    return False

