
import functools
import operator
def pilish_string(txt):
    newArr = []
    p = list(map(int, '314159265358979'))
    for x in range(len(txt) if len(txt) < 16 else 15):
        b = functools.reduce(operator.add, p[:x], 0)
        if txt[b:b + p[x]] == '': return ' '.join(newArr)
        if p[x] > len(txt[b:]):
            q = p[x] - len(txt[b:])
            newArr.append(txt[b:b + p[x]] + q * txt[-1])
            return ' '.join(newArr)
        newArr.append(txt[b:b + p[x]])
    return ' '.join(newArr)

