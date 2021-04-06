
import math
​
def quartic_equation(a, b, c):
    if c == 0:
        # 0 is a solution:
        return 1 if a * b >= 0 else 3
    D = b**2 - 4 * a * c
    if D < 0:
        return 0
    if D == 0:
        return 2
    z1 = (-b + math.sqrt(D)) / (2 * a)
    z2 = (-b - math.sqrt(D)) / (2 * a)
    if z1 < 0:
        return 0
    return 2 if z2 < 0 else 4

