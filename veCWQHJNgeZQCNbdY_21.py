
def root_digit(n):
    res = str(n)
    while len(str(res)) > 1:
        new = 0
        for i in res:
            new += int(i)
        res = str(new)
    return int(res)

