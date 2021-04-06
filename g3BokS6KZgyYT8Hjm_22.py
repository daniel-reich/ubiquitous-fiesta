
def shift_to_left(x, y, ans=2):
    if y == 0:
        return x
    if y == 1:
        return x*ans
    return shift_to_left(x, y-1, 2*ans)

