
def modulo(x, y):
    if y > 0:
        if x >= y:
            return modulo(x - y, y)
        if x <= -y:
            return modulo(x + y, y)
        return x
    else:
        if x >= -y:
            return modulo(x + y, y)
        if x <= y:
            return modulo(x - y, y)
        return x

