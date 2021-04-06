
from math import ceil
def cal(depth):
    if depth > 150 and depth < 300:
        return  ceil(6+(30 + 10) + (depth-150) / 5)
    elif depth >= 300 and depth < 450:
        return ceil((2*6) + (2 * (30 + 10) + (depth - 300)/5))
    else:
        return ceil(depth / 5)
#cal(300)

