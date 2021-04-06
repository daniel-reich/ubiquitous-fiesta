
def crazyfunction(a, b):
    aa = bin(a)[2:]
    bb = bin(b)[2:]
​
    bs = int(aa,2) ^ int(bb,2)
    return bs

