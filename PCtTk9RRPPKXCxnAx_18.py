
def modulo(x, y):
    c = 0
    if x < 0:
        c += 1
    if y < 0:
        c += 1
​
    if c == 1:
        if x < 0:
            if x > -y:
                return x
            else:
                return modulo(x+y,y)
        else:
            if x < abs(y):
                return x
            else:
                return modulo(x+y,y)
    elif c == 0:
        if x < y:
            return x
        else:
            return modulo(x-y,y)
    else:
        if x > y:
            return x
        else:
            return modulo(x-y,y)

