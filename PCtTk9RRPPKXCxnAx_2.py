
def modulo(x, y):
    rem = abs(x) - abs(y)
    if rem < 0: return x
    x = rem * x // abs(x)
    return x if abs(x) < abs(y) else modulo(x, y)

