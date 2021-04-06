
def point_in_triangle(p1, p2, p3, x, y):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    c = 1 - a - b
    return 0 < a < 1 and 0 < b < 1 and 0 < c < 1
​
def within_triangle(p1, p2, p3, test):
    return point_in_triangle(p1, p2, p3, test[0], test[1])

