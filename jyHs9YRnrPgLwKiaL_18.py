
import math
​
def split(x):
    if x == 1:
        return 1
    a = x / math.e
    p1 = math.floor(a)
    p2 = math.ceil(a)
    ans = max(pow(x / p1, p1), pow(x / p2, p2))
    return round(ans, 1)

