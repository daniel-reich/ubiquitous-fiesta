
def cal(depth):
    from math import ceil
    return ceil(depth / 5) + ((depth - 1) // 120) * 16 * (depth not in range(120, 151))

