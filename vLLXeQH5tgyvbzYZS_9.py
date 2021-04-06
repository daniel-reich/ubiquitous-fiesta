
def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a
​
def is_prim_pyth_triple(lst):
    a, b, c = sorted(lst)   
    triple = a**2 + b**2 == c**2
    primitive = max(gcd(a, b), gcd(a, c), gcd(b, c)) == 1
    return triple and primitive

