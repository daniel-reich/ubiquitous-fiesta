
import math
​
def sum_and_product(s, p):
    if s**2 - 4*p < 0:
           return None
    elif s**2 - 4*p == 0:
            return (round(s/2, 3), round(s/2, 3))
    else:
        y_1 = (s + math.sqrt(s**2 - 4 *p))/2
        y_2 = (s - math.sqrt(s**2 - 4 *p))/2
        x_1 = s - y_1
        x_2 = s - y_2
    return (round(min(x_1, x_2), 3), round(s - min(x_1, x_2), 3))

