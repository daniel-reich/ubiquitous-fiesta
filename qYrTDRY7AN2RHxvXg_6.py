
import math
​
def f(A, c):
    D = c**4 - 16 * A**2
    if D >= 0:
        side1 = round( math.sqrt( (c**2 - math.sqrt(D)) / 2), 3)
        side2 = round( math.sqrt( (c**2 + math.sqrt(D)) / 2), 3)
        return [side1, side2]
    else:
        return "Does not exist"

