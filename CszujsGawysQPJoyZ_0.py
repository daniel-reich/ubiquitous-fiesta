
import math
​
g = 9.81
pi = math.pi
​
def hit_prince(vo, th, yo, ds):
    h = yo
    a = th * pi / 180
    w = vo**2 * math.sin(2*a) / (2 * g) + vo * math.cos(a) * \
        math.sqrt(vo**2 * math.sin(a)**2 + 2 * g * h) / g
    return abs(w - ds) < .5

