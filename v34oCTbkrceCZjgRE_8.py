
import math
def shift_to_right(x, y):
    return shift_to_right(x / 2, y - 1) if y else math.floor(x)

