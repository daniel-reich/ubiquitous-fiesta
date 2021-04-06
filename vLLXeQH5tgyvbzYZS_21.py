
def gcd(a, b):
    if b > a:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a
​
​
def is_prim_pyth_triple(lst):
    lst.sort()
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        if gcd(lst[0], lst[1]) == gcd(lst[0], lst[2])\
                == gcd(lst[1], lst[2]) == 1:
            return True
    return False

