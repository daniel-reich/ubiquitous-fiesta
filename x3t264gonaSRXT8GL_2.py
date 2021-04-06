
def repeating_cycle(n):
    z = x = 1 * 9
    k = 1
    while z % n:
        z = z * 10 + x
        k += 1
        if k > n:
            return -1
​
    return k

