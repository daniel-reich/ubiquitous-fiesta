
def quad_sequence(lst):
    L = len(lst)
    newlst = [lst[0]]
    firstDiff = lst[1] - lst[0]
    nextDiff = lst[2] - lst[1]
    secondDiff = nextDiff - firstDiff
    nextnum = firstDiff + lst[0]
    newlst.append(nextnum)
    for x in range( 1, 2 * len(lst) - 1):
        firstDiff = nextnum - newlst[x-1]
        nextDiff = secondDiff + firstDiff
        nextnum = nextDiff + nextnum
        newlst.append(nextnum)
    return newlst[-L:]

