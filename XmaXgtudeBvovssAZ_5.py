
from math import atan, sin, pi
def red_area(r):
    d = pi / 2 - 2 * atan(0.5)
    return round(r * r * ((1 + sin(d)) / 2 - d) / 2, 3)

