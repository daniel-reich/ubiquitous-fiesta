
def scale_tip(l):
    ii = l.index('I')
    a = (list(l[:ii]))
    b = (list(l[ii+1:]))
    if sum(a)== sum(b):
        return "balanced"
    elif sum(a) > sum(b):
        return "left"
    else:
        return "right"

