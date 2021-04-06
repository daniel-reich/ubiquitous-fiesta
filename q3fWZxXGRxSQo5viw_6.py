
import math
​
def cal(depth):
    t = 0
    while depth > 0:
        if depth <= 150:
            t += math.ceil(depth / 5)
            break
        # climb:
        t += 30
        depth -= 150
        # rest:
        t += 10
        depth += 30
    return t

