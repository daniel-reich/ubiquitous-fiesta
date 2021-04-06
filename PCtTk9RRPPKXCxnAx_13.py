
def modulo(x, y):
    if x > 0 and y > 0:
        if x == y:
            return 0
        if x < y:
            return x
        else:
            return modulo(x - y, y)
    elif x > 0 and y < 0:
        if x == y * -1:
            return 0
        if x < y * -1:
            return x
        else:
            return modulo(x + y, y)
    elif x < 0 and y > 0:
        if x == y * -1:
            return 0
        if x * -1 < y:
            return x
        else:
            return modulo(x + y, y)
    elif x < 0 and y < 0:
        if x == y:
            return 0
        if x > y:
            return x
        else:
            return modulo(x - y, y)

