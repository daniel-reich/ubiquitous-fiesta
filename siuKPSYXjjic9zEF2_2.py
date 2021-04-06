
import math
​
PI = math.pi
thickness = 0.025 / 10.0
​
def foil(length):
    if length == 0:
        return 4.0
    d = 4.0     # diameter of current layer
    circ = PI * d
    while length >= 0:
        if length >= circ:
            d += 2 * thickness
            length -= circ
        elif length >= 0:
            d += thickness
            length -= .5 * circ
        circ = PI * d
    return round(d, 4)

