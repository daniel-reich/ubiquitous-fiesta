
import math
def cal(depth):
    if depth == 150:
        return 30
​
    e = 40*(depth // 120)
    a = depth % 120
    b = math.ceil(a / 5)
​
    return b + e

