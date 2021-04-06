
from math import atan2
​
def polygon(lst):
    x, y = zip(*lst)
    x_mid = sum(x)/len(lst)
    y_mid = sum(y)/len(lst)
    lst.sort(key=lambda x: atan2(x[1]-y_mid, x[0]-x_mid))
    
    pairs, total = zip(lst, lst[1:] + lst[:1]), 0
    for [x1, y1], [x2, y2] in pairs:
        total += x1*y2 - y1*x2
    
    return total/2

