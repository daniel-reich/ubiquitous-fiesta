
def is_ladder_safe(ladder):
    '''
    Returns True if the ladder is safe based on the criteria, otherwise False
    '''
    width = len(ladder[0])
    if width < 5:
        return False  # too narrow
​
    gap = lastgap = rungs = 0
    
    for i in range(1, len(ladder)-1): # ignore top & bottom
        s = ladder[i].count(' ')
        if s == width - 2:  # non-rung section
            gap += 1
            if gap > 2:
                return False  # too big a gap
        elif 0 < s < width - 2:
            return False  # broken rung
        else: # sound rung
            rungs += 1
            if rungs > 2 and lastgap != gap:
                return False
            elif rungs > 1:
                lastgap = gap
                gap = 0
​
    return True

