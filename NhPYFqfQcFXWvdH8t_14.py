
def mod_inv(n, m):
    mm = m
    y = 0
    x = 1
    if (m == 1):
        return 0
​
    while (n > 1):
        if m == 0:
            return False
        q = n // m
        t = m
​
        m = n % m
        n = t
        t = y
​
        y = x - q * y
        x = t
​
    if (x < 0) :
        x = x + mm
​
    return x

