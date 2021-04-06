
def quartic_equation(a,b,c):
    D = b**2 - 4 * a * c
    if D < 0:
        return 0
    elif D == 0:
        if -b / a > 0:
            return 2
        elif b == 0:
            return 1
        else:
            return 0
    else:
        if c / a < 0:
            return 2
        elif c == 0:
            if -b / a > 0:
                return 3
            else:
                return 1
        else:
            if -b / a > 0:
                return 4
            elif -b / a < 0:
                return 0
            else:
                return 2

