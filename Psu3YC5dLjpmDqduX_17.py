
from functools import reduce
import operator
import math
​
def polygon(lst):
​
    coords = lst
    center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), coords), [len(coords)] * 2))
    lst = sorted(coords, key=lambda coord: (-135 - math.degrees(math.atan2(*tuple(map(operator.sub, coord, center))[::-1]))) % 360)
​
    x = 0
    for i in range(len(lst)):
        x += lst[i][0]*lst[(i+1)%len(lst)][1]-lst[i][1]*lst[(i+1)%len(lst)][0]
        
    x = abs(x)
    x = x / 2
    return x

