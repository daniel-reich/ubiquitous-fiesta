
def base_n(base, values, num):
    if len(values) != base:
        return False
    res = ''
    num, remainder = divmod(num, base)
    res = str(values[remainder]) + res
    while num > 0:
        num, remainder = divmod(num, base)
        res = str(values[remainder]) + res
    return res

