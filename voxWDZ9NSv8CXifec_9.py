
def lemonade(bills):
    f, te, tw = 0, 0, 0
    if bills[0] != 5:
        return False
    for i in bills:
        if i == 5:
            f += 1
        elif i == 10:
            te += 1
            f -= 1
        elif i == 20:
            tw += 1
            if f >= 3 and te < 1:
                f -= 3
            else:
                te -= 1
                f -= 1
        if f < 0 or te < 0 or tw < 0:
            return False
    return True

