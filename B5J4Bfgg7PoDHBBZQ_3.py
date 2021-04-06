
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
​
​
def within_triangle(p1, p2, p3, test):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = test
    a = area(x1, y1, x2, y2, x3, y3)
    a1 = area(x1, y1, x2, y2, x4, y4)
    a2 = area(x1, y1, x3, y3, x4, y4)
    a3 = area(x2, y2, x3, y3, x4, y4)
    return a1 + a2 + a3 == a

