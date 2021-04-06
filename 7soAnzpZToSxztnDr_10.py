
def shift_left(x, y, k=0):
    if k == y:
        return x
    return shift_left(x, y, k + 1) * 2

