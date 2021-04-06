
def find_the_difference(s, t):
    slst, tlst = list(s), list(t)
    for x in slst:
        tlst.pop(tlst.index(x))
    return tlst[0]

