
import math
import math
​
def primeFactors(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            res.append(int(i))
            n = n / i
    if n > 2:
        res.append(int(n))
    x = 0
    rc = 0
    while True:
        rc += (len(str(res[x])) + len(str(res.count(res[x]))) if res.count(res[x]) > 1 else len(str(res[x])) )
        x += res.count(res[x])
        if x >= len(res): break
    return rc
​
​
def is_economical(n):
    r = (primeFactors(n))
    if r == len(str(n)): return 'Equidigital'
    if r < len(str(n)): return 'Frugal'
    return 'Wasteful'

