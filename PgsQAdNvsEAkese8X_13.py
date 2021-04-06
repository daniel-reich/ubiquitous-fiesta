
def to_list(dct):
    return [] if not dct else [list((key, val)) for key, val in sorted(dct.items())]

