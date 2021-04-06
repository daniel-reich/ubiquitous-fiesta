
from fractions import Fraction
​
def pascal_row(n):
    if n == 0:
        return [1]
    row = [1]
    f = Fraction(1, 1)
    for k in range(1, n):
        f *= Fraction(n + 1 - k, k)
        row.append(int(f))
    row.append(1)
    return row

