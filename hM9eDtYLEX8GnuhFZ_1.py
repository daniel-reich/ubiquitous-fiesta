
from fractions import gcd
def random(lst):
    fr, lr = lst 
    if lr == fr: return lr
    m, n = 65535, 0
    while True:
        a = (lr - 1  +  m * n) / fr
        if a % 1 == 0:
            a = int(a)
            break
        n += 1
    return None if a + m // gcd(m, fr) < m else (a * lr + 1) % m

