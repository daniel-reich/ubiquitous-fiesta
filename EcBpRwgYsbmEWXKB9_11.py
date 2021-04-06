
def prime(x):
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    r = int(x ** 0.5)
    f = 5
    while f <= r:
        if x % f == 0 or x % (f + 2) == 0:
            return False
        f += 6
    return True

