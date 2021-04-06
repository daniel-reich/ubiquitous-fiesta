
def wash_hands(N, nM):
    a = N * nM * 30 * 21
    b = a // 60
    c = a - (b * 60)
    return "{} minutes and {} seconds".format(b , c)

