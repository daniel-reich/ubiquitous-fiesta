
def euclidean(a, b):
    if a<b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    a = b
    b = r
    return euclidean(a, b)

