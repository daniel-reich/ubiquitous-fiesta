
def within_triangle(p1, p2, p3, test):
    (x1, y1), (x2, y2), (x3, y3) = sorted((p1, p2, p3), key=lambda x:(x[1]))
    d1 = (y2 - y1)*(test[0] - x1) + (-x2 + x1)*(test[1] - y1)
    d2 = (y3 - y2)*(test[0] - x2) + (-x3 + x2)*(test[1] - y2)
    d3 = (y1 - y3)*(test[0] - x3) + (-x1 + x3)*(test[1] - y3)
    return all(i >= 0 for i in (d1, d2, d3))

