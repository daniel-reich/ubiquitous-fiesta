
def is_ladder_safe(ldr):
    ldrWidth = len(ldr[0])
    width = ldr[0].count(" ")
    if width < 3: return False
    if ldrWidth < 5: return False
    rungs = []
    for x in range(len(ldr)):
        if ldr[x].count("#") > 2:
            rungs.append(x)
    if len(rungs) <= 1: return False
    distbtw = rungs[1] - rungs[0]
    if ldr[rungs[0]].count("#") != ldrWidth: return False
    for x in range(1, len(rungs)):
        if rungs[x] - rungs[x -1] != distbtw or rungs[x] - rungs[x -1] > 3   : return False
        if ldr[rungs[x]].count("#") != ldrWidth: return False
    return True

