
import itertools
from collections import Counter
​
def get_factors(n):
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
def express_factors(n):
    ans = ""
    C = Counter(list(get_factors(n)))
    keys = sorted(C.keys())
    ans = str(keys[0])
    c = C[keys[0]]
    if c > 1:
        ans += "^" + str(c)
    for p in keys[1:]:
        c = C[p]
        ans += " x " + str(p)
        if c > 1:
            ans += "^" + str(c)
    return ans

