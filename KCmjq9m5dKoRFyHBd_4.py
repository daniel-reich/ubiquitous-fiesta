
def which_side(poly, vert):
    # reverse order of vertices if orientation is clockwise
    if sum([(p2[0]-p1[0])*(p2[1]+p1[1]) for p1, p2 in zip(poly, (poly+[poly[0]])[1:])]) > 0:
        poly = poly[::-1]
    vi, pl = poly.index(vert), len(poly)
    # translate preceding, target and succeeding points so that preceding is origin (0, 0)
    x1, y1 = poly[vi-1][0], poly[vi-1][1]
    x2, y2, x3, y3 = vert[0] - x1, vert[1] - y1, poly[(vi+1)%pl][0] - x1, poly[(vi+1)%pl][1] - y1
    # determinant of succeeding and target point vectors determines whether target is 
    # left or right of line joining preceding (origin) to succeeding
    return 'reflex' if (x3 * y2 - y3 * x2) > 0 else 'regular'

