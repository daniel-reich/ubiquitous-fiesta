
def order(lst):
    return [i[1] for i in sorted([i[::-1] for i in enumerate(lst)])]

