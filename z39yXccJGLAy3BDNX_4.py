
def flipping_bits(n):
    res = 0
    for i in range(32):
        if not n & 1:
            res += pow(2, i)
        n >>= 1
    return res

