
import math
def convert(slope):
    a = round(math.degrees(math.atan(slope)))
    if a >= 0:
        return 90 - a
    else:
        return 90 + abs(a)

