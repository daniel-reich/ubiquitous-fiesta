
def remap(n, a, b, c, d):
    return 0 if a == b else c+(n-a)*(d-c)/(b-a)

