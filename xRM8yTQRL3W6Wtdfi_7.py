
def quartic_equation(a, b, c):
    d2 = b * b - 4 * a * c
    count = 0
    if d2 >= 0:
        d = pow(d2, 0.5)
        if -b + d > 0:
            count += 2
        if -b - d > 0:
            count += 2
        if -b + d == 0:
            count += 1
        if -b - d == 0:
            count += 1
    return count

