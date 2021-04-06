
from itertools import groupby
def validate(s):
    a, c = [], []
    clusters = [[1,3,3,4],[3,3,4]]
    valid = ' -()/.+'
    for key, group in groupby(s, key=lambda x: x.isdigit()):
        if key:
            a.append(list(group))
        else:
            container = list(group)
            c.extend(container)
            if c[-1] not in valid:
                return False
            if len(container) > 1 and container[0] == container[1]:
                return False
    
    if not c:
        d = sum(a, [])
        if len(d) == 11 or len(d) == 10:
            return True
​
    return [len(x) for x in a] in clusters and not(not s[0].isdigit() and s[0] not in valid)

