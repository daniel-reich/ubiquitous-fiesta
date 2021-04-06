
def little_big(n):
    if n % 2 == 0:
        x = n // 2
        ctr = 50
        for i in range(x):
            ctr *= 2
        return ctr
    else:
        x = n // 2 + 1
        ctr = 4
        for i in range(x):
            ctr += 1
        return ctr

