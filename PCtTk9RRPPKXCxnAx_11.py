
def modulo(x, y, s=None):
    if not s: s=x//abs(x)
    return modulo((abs(x)-abs(y))*s, y, s) if abs(x) >= abs(y) else x

