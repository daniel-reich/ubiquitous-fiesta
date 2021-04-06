
import itertools
​
def factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n
​
def get_sums(pfacs, n):
    sums = set(pfacs)
    queue = pfacs[:]
    while len(queue) > 0:
        cur = queue.pop(0)
        for pf in pfacs:
            s = cur + pf
            if s <= n and s not in sums and s not in queue:
                sums.add(s)
                queue.append(s)
    return sums
​
def c_fuge(n, k):
    if n == 1:
        return False
    if n == k:
        return True
    if k > n:
        return False
    pfacs = list(set(factors(n)))
    diff = n - k
    sums = get_sums(pfacs, n)
    return k in sums and diff in sums

