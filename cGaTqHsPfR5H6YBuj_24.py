
def make_sandwich(i, f):
    lst = []
    for ind in i:
        if ind != f:
            lst.append(ind)
        else:
            lst.append('bread')
            lst.append(f)
            lst.append('bread')
    return lst

