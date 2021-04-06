
import math
def cal(depth):
    if depth <= 150:
        return math.ceil(depth / 5)
    else:
        return math.ceil((depth + depth//150 * 30) / 5 + 10 * (depth//150))

