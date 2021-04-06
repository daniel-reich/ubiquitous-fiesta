
def split(n):
    if n >= 3:
        r = n%3; d= n//3; v = 3**(n//3)
        return 3**(d -1)*4 if r == 1 else v*2 if r == 2 else v
    return n

