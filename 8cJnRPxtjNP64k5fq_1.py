
def dance(lst, param):
    w, m = zip(*lst)
    if param == 'men':
        return [list(i) for i in zip(w, reversed(m))]
    return [list(i) for i in zip(reversed(w), m)]

