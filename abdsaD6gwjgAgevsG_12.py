
def power_ranger(n, a, b):
    e = 0
    if a < b:
        for i in range(a, b + 1):
            if (i**(1/n)) % 1 != 0:
                pass
            else:
                e += 1
    return e

