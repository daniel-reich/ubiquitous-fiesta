
def gcd_order(a, b):
    if b % a == 0:
        return a
    else:
        return gcd_order(b % a, a)
​
​
def gcd(a, b):
    if a > b:
        return gcd_order(b, a)
    return gcd_order(a, b)
​
def sim_prop_frac(max_den):
    if max_den == 1:
        return 0
    if max_den == 2:
        return 1
    cnt = 0
    for num in range(1, max_den):
        if gcd(num, max_den) == 1:
            cnt += 1
    return cnt + sim_prop_frac(max_den-1)

