
import re
​
def eval_algebra(s):
    s = s.replace(' ', '').replace('=', '==')
    a, b = map(int, re.findall(r'-? ?\d+', s))
    if eval(s.replace('x', str(a-b))):
        return a - b
    elif eval(s.replace('x', str(b-a))):
        return b - a
    return a + b

