
def accum(txt):
    return "-".join([(l*(txt.index(l)+1)).capitalize() for l in txt])

