
from math import sqrt
​
def dist(line, x, y):
    imp = line.split('=')[1]
    a = eval(imp[0:imp.index('x')])
    c = eval(imp[imp.index('x') + 1:])
    return round((abs(a*x + c - y))/(sqrt(a*a+1)), 2)

