
def accum(txt):
    return '-'.join([c.upper() + (c*i).lower() for i, c in enumerate(txt)])

