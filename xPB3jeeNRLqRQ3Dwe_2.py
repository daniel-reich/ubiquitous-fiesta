
def find_None(lst):
    for idx, i in enumerate(lst):
        if i is None:
            return idx
    return -1

