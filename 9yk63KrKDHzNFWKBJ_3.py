
def is_it_inside(folders,X,Y):
    while X != Y:
        f = [k for (k, v) in folders.items() if X in v]
        if not f:
            return False
        X = f[0]
    return True

