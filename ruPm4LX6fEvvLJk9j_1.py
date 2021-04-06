
import numpy as np
​
def esthetic(n):
    res = []
    for base in range(2, 11):
        num = np.base_repr(n, base)
        if all(abs(int(a) - int(b)) == 1 for a, b in zip(num, num[1:])):
            res.append(base)
    return res if res else 'Anti-Esthetic'

