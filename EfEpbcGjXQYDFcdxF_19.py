
def filter_list(l):
    new = []
    for x in l:
        if isinstance(x, int):
            new.append(x)
    return new

