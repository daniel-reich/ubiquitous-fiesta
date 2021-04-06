
import math
def shortestDistance(txt):
    lst = list(map(lambda x: int(x), txt.split(',')))
    a = lst[:2]
    b = lst[2:]
    
    return round(((abs(a[0]-b[0])**2) + (abs(a[1]-b[1])**2))**0.5, 2)

