
def natural_position(n):
    if n < 10: return n
    nd = len(str(n))
    return 10 + nd * (n - 10**(nd-1)) + sum((9 * 10**i) * (i + 1) for i in range(1, nd - 1))
​
def is_early_bird(_range, n):
    seq = ''.join(str(i) for i in range(_range + 1))
    lst = []
    pos = seq.find(str(n))
    isearly = pos < natural_position(n)
    while pos >= 0:
        lst.append([ix for ix in range(pos, pos + len(str(n)))])
        pos = seq.find(str(n), pos+1)
    if isearly: lst.append('Early Bird!')
    return lst

