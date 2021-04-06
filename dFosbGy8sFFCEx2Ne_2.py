
from collections import Counter
​
def rank(lst):
    C = Counter(lst)
    n = len(lst)
    L = [[lst[i], i] for i in range(n)]
    L.sort(key = lambda x: (x[0], x[1]))
    positions = {L[i][1]: i for i in range(n)}
    ans, memo = [], {}
    for i in range(n):
        k = lst[i]
        pos = positions[i]
        c = C[k]
        if c == 1:
            ans.append(pos)
        else:
            if k in memo:
                ans.append(memo[k])
            else:
                ra = (pos * c + c * (c - 1) // 2) / float(c)
                memo[k] = ra
                ans.append(ra)
    return ans

