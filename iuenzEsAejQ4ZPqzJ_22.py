
def mystery_func(num):
    i = 0
    while True:
        if 2**i > num:
            break
        else:
            i += 1
    i -= 1
    rem = num - 2**i
    res = ""
    for j in range(0, i):
        res += "2"
    res += str(rem)
    return int(res)

