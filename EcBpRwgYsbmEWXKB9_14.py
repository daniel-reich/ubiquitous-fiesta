
def prime(x):
    if x & 1 == 0:
        return False
    d = 3
    while d * d <= x:
        if x % d == 0:
            return False
        d = d + 2
    return True

