
def deepest(lst):
    counter = []
    for i in lst:
        if isinstance(i, list):
            counter.append(deepest(i))
    if len(counter) > 0:
        return 1 + max(counter)
    return 1

