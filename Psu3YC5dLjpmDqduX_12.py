
from math import asin, pi
​
​
def polygon(lst):
    res = lst
    if len(lst) > 3:
        center_x = sum(p[0] for p in lst) / len(lst)
        center_y = sum(p[1] for p in lst) / len(lst)
​
        def angle_from_center(p):
            x = p[0] - center_x
            y = p[1] - center_y
            angle = asin(abs(y) / (x * x + y * y) ** 0.5)
            if x < 0 <= y:
                angle = pi - angle
            elif x < 0 and y < 0:
                angle += pi
            elif y < 0 <= x:
                angle = 2 * pi - angle
            return angle
        lst.sort(key=angle_from_center)
    area = 0
    for i in range(len(res) - 1):
        area += res[i][0] * res[i + 1][1] - res[i][1] * res[i + 1][0]
    area += res[len(res) - 1][0] * res[0][1] - res[len(res) - 1][1] * res[0][0]
    return abs(area) / 2

