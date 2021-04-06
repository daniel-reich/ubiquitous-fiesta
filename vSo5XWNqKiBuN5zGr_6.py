
def divide(x, y, n = 0):
    sign = -1 if x * y < 0 else 1
    return n * sign if abs(x) < abs(y) else divide(x - sign*y, y, n+1)

