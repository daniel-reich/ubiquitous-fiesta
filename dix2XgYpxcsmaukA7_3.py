
def express_factors(n):
    res, i = {}, 2
    while i<=n:
        while n % i == 0:
            res[i] = res.get(i, 0) + 1
            n //= i
        i += 1
    return ' x '.join(str(n) if res[n]==1 else '%d^%d' % (n,res[n])\
                      for n in sorted(res))

