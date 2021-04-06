
def extended_euclid(a, b):
    if a == 0:
        return (b, 0, 1)
    d, y, x = extended_euclid(b%a, a)
    return (d, x - b//a*y, y)
​
def mod_inv(n, m):
    d, x, _ = extended_euclid(n, m)
    return x%m if d == 1 else False

