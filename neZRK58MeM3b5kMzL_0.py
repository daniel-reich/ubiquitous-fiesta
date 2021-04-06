
import math
​
PI = math.pi
r = 5.0
​
def height_needed(volume):
    # V = pi * r**2 * h / 3
    height = 3.0 * 1000.0 * volume / (r**2 * PI)
    return round(height, 2)

