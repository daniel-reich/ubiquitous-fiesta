
def accum(txt):
    return '-'.join([(n * ch).title() for n, ch in enumerate(txt, 1)])

