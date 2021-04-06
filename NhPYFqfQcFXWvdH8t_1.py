
def mod_inv(a, b, c=0, d=1):
    if b == 0: return a == 1 and d
    return mod_inv(b, a -a//b*b, d -a//b*c, c)

