
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
​
​
def mod_inv(a, m):
    if gcd(a, m) != 1:
        return False
    x1, x2, x3 = 1, 0, a
    y1, y2, y3 = 0, 1, m
    while y3 != 0:
        q = x3 // y3
        y1, y2, y3, x1, x2, x3 = (
            x1 - q * y1), (x2 - q * y2), (x3 - q * y3), y1, y2, y3
    return x1 % m

