
def modulo(x, y):
    if (abs(x) < abs(y)): return x
    if (x * y > 0): return modulo(x-y, y)
    else : return modulo(x+y, y)

