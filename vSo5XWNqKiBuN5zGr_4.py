
def divide(x, y, res=0):
    if abs(x) < abs(y):
        return res if x * y >= 0 else -res
    return divide(x - y, y, res + 1) if x * y > 0 else divide(x + y, y, res + 1)

