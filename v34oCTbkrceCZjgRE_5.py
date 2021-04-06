
import math
def shift_to_right(x, y, ans = 2):
    if y == 0:
        return x
    if y == 1:
        return math.floor(x/ans)
    return shift_to_right(x, y-1, ans*2)

