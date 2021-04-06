
def int_to_vlq(n):
    if n < 128:
        return [n]
    for k in range(1, 20):
        if n == 128**k:
            return [129] + [128] * (k-1)+ [0]
    k = 0
    while n > 128**k:
        k += 1
    k -= 1
    seq = []
    while k >= 1:
        d = n // (128**k)
        seq.append(d + 128)
        n -= d * 128**k
        k -= 1
    seq.append(n % 128)
    return seq
​
def vlq_to_int(lst):
    n = lst[-1]
    l = len(lst)
    power = 1
    for k in range(1, l):
        power *= 128
        n += power * (lst[l - 1 - k] - 128)
    return n

