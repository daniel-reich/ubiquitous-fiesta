
def deepest(lst):
    if isinstance(lst, list) and len(lst) != 0:
        return 1 + max(deepest(x) for x in lst)
    else:
        return 0

