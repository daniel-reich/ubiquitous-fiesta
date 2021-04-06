
def quartic_equation(a, b, c):
    x1 = (-b + (b**2 - 4 * a * c)**.5) / (2 * a)
    x2 = (-b - (b**2 - 4 * a * c)**.5) / (2 * a)
​
    myans = 0
    if x2 == 0:
        myans += 1
    if x2 > 0:
        myans += 2
    if x1 == 0:
        myans += 1
    if x1 > 0:
        myans += 2
​
    return myans

