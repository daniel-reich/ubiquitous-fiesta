
def base_n(base, values, num):
    if len(values) != base: return False
    res = []
    while num > 0:
        num, r = divmod(num, base)
        res.append(str(values[r]))
    return ''.join(res[::-1])

