
def is_prim_pyth_triple(lst):
    from fractions import gcd
    a, b, c = sorted(lst)
    if not a ** 2 + b ** 2 == c ** 2:
        return False
    else:
        gc = gcd(a, b)
        if c % gc == 0 and gc > 1:
            return False
        else:
            return True

