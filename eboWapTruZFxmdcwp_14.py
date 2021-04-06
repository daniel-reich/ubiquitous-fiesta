
def is_positive_dominant(lst):
    negs = {}
    pos = {}
    for l in lst:
        if l > 0:
            pos[l] = None
        elif l<0:
            negs[l] = None
    return len(pos) > len(negs)

