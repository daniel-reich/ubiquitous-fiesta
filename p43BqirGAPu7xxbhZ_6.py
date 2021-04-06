
from itertools import chain
​
def diamond(crt):
    res = []
    for i in chain(range((crt-1) // 2, 0, -1), range((crt+1) // 2)):
        row = [0] * crt
        row[-i-1] = row[i] = 1
        res.append(row)
    return [res, ( "good cut", "perfect cut")[crt % 2]]

