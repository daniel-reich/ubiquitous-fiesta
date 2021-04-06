
def divide(x, y, sign=1):
    if x == 0:
        return 0
    sign = x * y // abs(x * y)
    x = abs(x)
    y = abs(y)
    if x < y:
        return 0
    return sign * (1 + divide(x - y, y, sign))

