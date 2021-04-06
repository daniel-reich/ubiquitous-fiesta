
from math import pi
def foil(length, r=2, h=0.0025):
    half_wraps = 0
    while length > 0:
        length -= pi * (r + h * (half_wraps // 2))
        half_wraps += 1
    return round(2 * r + h * half_wraps, 4)

