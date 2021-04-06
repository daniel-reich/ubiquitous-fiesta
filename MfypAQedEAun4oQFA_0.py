
def perrin(n):
    start = [3, 0, 2]
    if n < 3: return start[n]
    return perrin(n-2) + perrin(n-3)

