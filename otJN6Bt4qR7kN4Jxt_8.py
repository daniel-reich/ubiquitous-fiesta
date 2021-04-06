
def incremental_depth(x):
    if len(x) == 1:
        print("innermost elem.:", x)
        return x
    return [x[0],incremental_depth(x[1:])]

