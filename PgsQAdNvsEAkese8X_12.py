
def to_list(dct):
    l = []
    for key in dct:
        l.append([key, dct[key]])
    return sorted(l)

