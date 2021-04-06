
def is_happy(n, seq=[]):
    if n == 1:
        return True
    if n == 4:
        return False
    m = 0
    while n > 0:
        m += (n % 10)**2
        n //= 10
    n = m
    seq.append(n)
    return is_happy(n, seq)

