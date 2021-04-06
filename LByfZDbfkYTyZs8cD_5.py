
import math
def areaofhexagon(x):
    a = round((3 * math.sqrt(3) * (x * x)) / 2, 1)
    if x <= 0: return None
    return a

