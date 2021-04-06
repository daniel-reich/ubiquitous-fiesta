
def cup_swapping(swaps):
    l = "B"
    for x in swaps :
        if l in x:
            if x[0] != l: l = x[0]
            else: l = x[1]
    return l

