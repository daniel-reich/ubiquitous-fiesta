
def blocks(a):
    b = 7
    c = 5
    if a == 0:
        return 0
    elif a == 1:
        return 5
    else:
        for x in range(a-1):
            c += b
            b += 1
        return c

