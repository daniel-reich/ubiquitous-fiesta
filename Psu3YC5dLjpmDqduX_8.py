
from math import pi, atan2
from functools import reduce
def polygon(lst):
    # calculate avarage of points
    x,y = reduce(lambda p1, p2: (p1[0]+p2[0], p1[1]+p2[1]), lst)
    p0 = [x/len(lst), y/len(lst)]
    # sort by angle 
    lst.sort(key=lambda p: ((atan2(p0[1]-p[1], p0[0]-p[0]) * 180 / pi) + 360)%360)
    # apply polygon area formula 
    return abs(sum(p1[0]*p2[1] - p2[0]*p1[1] for p1, p2 in zip(lst, lst[1:] + [lst[0]]))) / 2

