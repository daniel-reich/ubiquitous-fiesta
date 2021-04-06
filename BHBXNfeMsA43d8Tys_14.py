
#modified spigot algorithm
#more info at https://groups.google.com/forum/#!msg/mathfuture/LA0pMPC6-HE/MBGWxn4ENsUJ
​
def pi(n):
    n += 1
    res = ''
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while n > 0:
        p, q, k = k**2, 2*k + 1, k + 1
        a, b, a1, b1 = a1, b1, p*a + q*a1, p*b + q*b1
        d, d1 = a / b, a1 / b1
        while d == d1 and n > 0:
            res += str(int(d))
            n -= 1
            a, a1 = a%b * 10, a1%b1 * 10
            d, d1 = a/b, a1/b1
    return '3.' + res[1:]

