
from math import factorial as f
def pascals_triangle(row):
    x = []
    for col in range(row + 1):
        x.append(str(f(row)//(f(col)*f(row-col))))
    return ' '.join(x)

