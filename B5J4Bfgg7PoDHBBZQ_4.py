
def within_triangle(p1, p2, p3, test):
    a = (p2[0]-p1[0], p2[1]-p1[1])
    b = (p3[0]-p1[0], p3[1]-p1[1])
    v = (test[0]-p1[0], test[1]-p1[1])
    D = a[0] * b[1] - b[0] * a[1]
    Ds = v[0] * b[1] - b[0] * v[1]
    Dt = a[0] * v[1] - v[0] * a[1]
    s = Ds / D
    t = Dt / D
    return s >= 0 and t >= 0 and s + t <= 1

