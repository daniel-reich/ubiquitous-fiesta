
from collections import Counter
def is_economical(n):
    fact = []
    l_num = len(str(n))
    for x in range(2, n + 1):
        while n % x == 0:
            fact.append(x)
            n /= x
​
    fact = Counter(fact)
​
    keys = list(fact.keys())
​
    ln = sum([len(str(x)) + len(str(fact[x])) if fact[x] > 1 else len(str(x)) for x in keys])
​
    return 'Equidigital' if l_num == ln else 'Frugal' if l_num > ln else 'Wasteful'

