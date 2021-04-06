
def euclidean(a, b):
    if a == b:
        return a
    else:
        if b > a:
            a, b = b, a
        return euclidean(b, a-b)

