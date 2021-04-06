
from math import ceil
def ulam(n):
    us = {1,2}
    ul = [1,2]
    m = 2
    while len(ul) < n:
        m += 1
        count, i = 0, 0
        while ul[i] < m /2:
            if m - ul[i] in us:
                count += 1
            i += 1
        if count == 1:
            us.add(m)
            ul.append(m)
    return ul[n-1]

