
import math
​
def f(A, c):
    D = c**4 / 4. - 4 * A**2
    if D < 0:
        return "Does not exist"
    a = math.sqrt(c**2 / 2. + math.sqrt(D))
    a2 = math.sqrt(c**2 / 2. - math.sqrt(D))
    b = 2 * A / a
    return sorted([round(a, 3), round(b, 3)])

