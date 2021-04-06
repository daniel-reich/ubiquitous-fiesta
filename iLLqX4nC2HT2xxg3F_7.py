
def deepest(lst):
    if isinstance(lst, list):
        return 1 + max(deepest(item) for item in lst)
    else:
        return 0

