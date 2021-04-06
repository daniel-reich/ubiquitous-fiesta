
from math import ceil, sqrt
​
def encryption(txt):
​
    txt = txt.replace(' ', ''); col = ceil(sqrt(len(txt)))
​
    lst = []; lvl = col
    for i in range(0, len(txt), col):
        lst.append(txt[i:lvl])
        lvl += col
​
    res = ''
    for j in range(len(lst[0])):
        for i in range(len(lst)):
            if j < len(lst[i]):
                res += lst[i][j]
        res += ' '
​
    return res.rstrip()

