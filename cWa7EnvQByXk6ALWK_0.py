
def golden_ratio():
    a, b = 1, 1
    while len(str(b)) < 100:
        a, b = b, a + b
    return '1.' + str((b * 10 ** 100) // a)[1:100]

