
def modulo(x, y):
    if x == y:
        return 0
    if abs(x) > abs(y):
        return modulo(x - y, y) if x * y > 0 else modulo(x + y, y)
    return x

