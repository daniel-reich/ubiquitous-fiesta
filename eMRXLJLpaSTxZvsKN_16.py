
def is_ladder_safe(ldr):
    if len(ldr[0])<5:
        return False           # not a ladder or too short
    # since i don't need top and bottom element, they are removed
    ldr.pop(0), ldr.pop(-1)
    # broken rung
    if any(Z.count('#') in range(3, len(ldr[0])) for Z in ldr):
        return False      
    # calculate distance between rungs
    lw = list(enumerate([1 if all(Z=='#' for Z in Y) else 0 for Y in ldr]))
    # only rungs with position
    lw2 = [Z for Z in lw if Z[1] == 1]
    # no rungs
    if len(lw2)==0:
        return False
    d0 = lw2[1][0]-lw2[0][0]
    # if distance between rungs is greated than 3, 
    # or spaces between them are greater than 2
    if d0 > 3:
        return False
    # calculate equidistance
    for i in range(2,len(lw2)):
        if lw2[i][0] - lw2[i-1][0] != d0:
            return False
    return True

