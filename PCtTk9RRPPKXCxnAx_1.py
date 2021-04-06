
def modulo(x, y):
    if abs(x) < abs(y):
        return x
    elif y < 0 and x > 0 or y > 0 and x < 0:
        return modulo(x + y, y)
    elif y > 0 and x > 0 or y < 0 and x < 0:
        return modulo(x - y, y)

