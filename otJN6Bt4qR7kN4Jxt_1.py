
def incremental_depth(lst):
    res = [lst.pop()]
    while lst:
        res = [lst.pop(), res]
    return res

