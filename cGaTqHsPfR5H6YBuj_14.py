
def make_sandwich(i, f):
    lst = []
    for x in i:
        if x == f:
            lst.append('bread')
            lst.append(x)
            lst.append('bread')
        else:
            lst.append(x)
    return lst

