
def round_number(num, n):
    lower = 0
    i = 1
    while True:
        x = i * n
        if x < num:
            lower = x
        else:
            upper = x
            break
        i += 1
    if num - lower < upper - num:
        return lower
    return upper

