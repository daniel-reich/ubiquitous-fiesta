
def cal(depth):
    import math
    if depth <= 150:
        return math.ceil(depth / 5)
    tot = 0
    while depth - 150 > 0:
        depth -= 120
        tot += 40
    tot += depth / 5
    return math.ceil(tot)

