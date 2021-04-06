
from math import pi
import sys
sys.setrecursionlimit(4000)
​
def foil(length, d=4):
    if length <= 0:
        return round(d - 0.0025,4) if -.5*d*pi > length else round(d, 4)
    else:
        return foil(length - d * pi, d + 0.005)

