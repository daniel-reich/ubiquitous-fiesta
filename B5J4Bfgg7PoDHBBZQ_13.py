
def within_triangle(p1, p2, p3, test):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    x = test[0]
    y = test[1]
    denominator = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    if denominator == 0: return False
    a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / denominator
    b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / denominator
    c = 1 - a - b
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

