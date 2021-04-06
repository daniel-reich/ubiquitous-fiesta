
import math
​
def convert(slope):
    if slope == 0:
        return 90
    a = math.atan(1 / slope) * (180 / math.pi)
    if a < 0:
        a += 180
    return round(a)

