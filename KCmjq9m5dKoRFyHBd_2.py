
import math
​
def which_side(poly, vert):
    n = len(poly)
    k = poly.index(vert)
    at_ver = clock_angle(*[poly[(k+i) % n] for i in [-1, 0, 1]])
    glob = sum(clock_angle(*[poly[(k+i) % n] for i in [-1, 0, 1]]) for k in range(n))
    return 'regular' if at_ver*glob > 0 else 'reflex'
​
def clock_angle(p1, p2, p3):
    (x1, y1) = p1
    (x2, y2) = p2
    (x3, y3) = p3
    vx, vy = x2-x1, y2-y1
    wx, wy = x3-x2, y3-y2
    sign = 1 if vx*wy-vy*wx > 0 else -1
    angle = math.acos((vx*wx+vy*wy)/((vx**2+vy**2)**.5*(wx**2+wy**2)**.5))
    return sign*angle

