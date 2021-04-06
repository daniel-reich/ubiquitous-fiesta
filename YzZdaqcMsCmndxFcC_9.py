
import collections
Point = collections.namedtuple("Point", "x y")
​
def centroid(x1, y1, x2, y2, x3, y3):
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    ordered = sorted([p1, p2, p3], key=lambda p: p.x + p.y)
    slope = (ordered[2].y - ordered[0].y)/(ordered[2].x - ordered[0].x)
    b = ordered[0].y - ordered[0].x * slope
    if ordered[1].y == ordered[1].x * slope + b:
        return False
    else:
        cx = (x1 + x2 + x3)/3
        cy = (y1 + y2 +y3)/3
        return (round(cx, 2), round(cy, 2))

