
def extended_gcd(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t
​
def mod_inv(a, m):
    b, x, y = extended_gcd(a, m)
    return ((1 - m * y) // a) % m if b == 1 else False

