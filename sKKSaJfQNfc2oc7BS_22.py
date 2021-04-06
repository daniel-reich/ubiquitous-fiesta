
def sle(m):
    a, b, c, d, e, f = m[0] + m[1]
    if a == b * d / e:
        return False
    x = int((c - b * f / e) / (a - b * d / e))
    y = int(f / e - d / e * x)
    return x, y

