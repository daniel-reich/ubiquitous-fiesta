
def order(lst):
    return [x[1] for x in sorted([[val, i] for i, val in enumerate(lst)])]

