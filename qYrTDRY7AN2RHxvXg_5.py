
from math import sqrt
def f(A, c):
    if c**4 - 16*A**2 < 0:
        return 'Does not exist'
    else:
        height = sqrt((c**2 + sqrt(c**4 - 16*A**2))/2)
        base = sqrt(c**2 - height**2)
        rheight = round(height, 3)
        rbase = (round(base, 3))
        if rheight < rbase:
            return [rheight, rbase]
        else:
            return [rbase, rheight]

