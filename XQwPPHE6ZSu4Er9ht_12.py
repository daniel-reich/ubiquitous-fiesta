
def is_economical(n):
    factors = []
    i ,k = 2,len(str(n))
    while n != 1:
        if n % i == 0:
            factors.append(i)
            n //= i
            i = 2
        else:
            i += 1
    count = [len(str(factors.count(i))) if factors.count(i) > 1 else 0 for i in set(factors)]
    ans = sum(count) + sum(len(str(i)) for i in set(factors))
    if ans == k:
        return 'Equidigital'
    if ans < k:
        return'Frugal'
    return 'Wasteful'

