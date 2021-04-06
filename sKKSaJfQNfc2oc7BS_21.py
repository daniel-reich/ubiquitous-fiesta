
def sle(m):
    a = m[0][0]
    b = m[0][1]
    c = m[0][2]
    d = m[1][0]
    e = m[1][1]
    f = m[1][2]
    D = a * e - b * d
    Dx = c * e - b * f
    Dy = a * f - c * d
    if D == 0:
        return False
    else:
        x = Dx / D
        y = Dy / D
        return (x, y)

