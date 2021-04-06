
def shift_left(x, y):
    if y == 0:
        return x
    return shift_left(2 * x, y - 1)

