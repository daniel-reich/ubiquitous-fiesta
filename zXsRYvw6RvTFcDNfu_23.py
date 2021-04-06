
def factorize(n):
    factors = []
    f = 2
    while f <= n:
        if n % f == 0:
            factors.append(f)
            n = n/f
        else:
            f += 1
    return factors
​
def ruth_aaron(n):
    factors_n = factorize(n)
    for m in [n-1, n+1]:
        factors_m = factorize(m)
        if len(factors_n) == len(set(factors_n)) and len(factors_m) == len(set(factors_m)):
            if sum(factors_n) == sum(factors_m):
                return ["Aaron", 3] if m < n else ["Ruth", 3]
        else:
            if sum(set(factors_n)) == sum(set(factors_m)):
                return ["Aaron", 1] if m < n else ["Ruth", 1]
            if sum(factors_n) == sum(factors_m):
                return ["Aaron",  2] if m < n else ["Ruth", 2]
    return False

