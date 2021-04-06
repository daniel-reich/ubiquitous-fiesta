
def gcd_ex(a, b):
    x, pre_x, y, pre_y, r, pre_r = 0, 1, 1, 0, a, b
    while r != 0:
        q = pre_r // r
        pre_r, r = r, pre_r - q * r
        pre_x, x = x, pre_x - q * x
        pre_y, y = y, pre_y - q * y
    return (pre_r, pre_x, pre_y)
​
def mod_inv(n, m):
    gcd, x, y = gcd_ex(n, m)
    return (y if y >= 0 else m + y) if gcd == 1 else False

