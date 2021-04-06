
def incremental_depth(lst):
    lst[-1:] = [lst[-1:]]
    return recurse(lst)
def recurse(lst, i=2):
    if len(lst) == 2:
        return lst
    lst[-i:] = [lst[-i:]]
    return recurse(lst)

