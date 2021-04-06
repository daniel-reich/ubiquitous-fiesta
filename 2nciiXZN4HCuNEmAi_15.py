
def flatten(r):
    if not isinstance(r, list): return [r]
    lst = []
    for e in r:
        if not isinstance(r, list):
            lst.append(e)
        else:
            lst.extend(flatten(e))
    return lst

