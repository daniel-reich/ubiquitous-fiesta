
def edge_sum(poly):
    S = 0
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1)%len(poly)]
        S += (x2 - x1) * (y2 + y1)
    return S
​
def is_to_the_left(p1, p2, p3):
    # determine whether point p3 is to the left from the line from p1 to p2
    position = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    return position < 0
​
def which_side(poly, vert):
    i2 = poly.index(vert)
    i1 = (i2 - 1) % len(poly)
    i3 = (i2 + 1) % len(poly)
    v1, v2, v3 = poly[i1], poly[i2], poly[i3]
    clockwise = edge_sum(poly) > 0
    left = is_to_the_left(v1, v2, v3)
    if clockwise:
        return "regular" if left else "reflex"
    else:
        return "reflex" if left else "regular"

