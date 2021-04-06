
from collections import Counter
​
def get_midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2., (p1[1] + p2[1]) / 2.)
​
def is_parallelogram(lst):
    midpoints = []
    for i in range(4):
        for j in range(i + 1, 4):
            midpoints.append(get_midpoint(lst[i], lst[j]))
    C = Counter(midpoints)
    return 2 in C.values() and len(C.keys()) == 5

