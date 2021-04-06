
def make_sandwich(i, f):
    nl = []
    for x in i:
        if x in f:
            nl.extend(['bread', x, 'bread'])
        else:
            nl.append(x)
    return nl

