
from math import atan2
def is_parallelogram(lst):
    x, y = zip(*lst)
    x_mid = sum(x) / len(lst)
    y_mid = sum(y) / len(lst)
    lst.sort(key=lambda p: atan2(p[1] - y_mid, p[0] - x_mid))
    x, y = zip(*lst)
    sides = [((x[i] - x[(i + 1) % len(x)]) ** 2
              + (y[i] - y[(i + 1) % len(x)]) ** 2) ** 0.5
             for i in range(len(x))]
    return sides[0] == sides[2] and sides[1] == sides[3]

