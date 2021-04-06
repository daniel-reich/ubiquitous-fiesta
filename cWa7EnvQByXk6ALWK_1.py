
def golden_ratio():
    a, b = 1, 1
    for k in range(10**4):
        a, b = b, a + b
    b *= 10**100
    g = b // a
    r = str(g)[0] + '.' + str(g)[1:-1]
    return r

