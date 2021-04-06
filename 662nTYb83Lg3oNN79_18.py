
from itertools import combinations
​
def is_parallelogram(lst):
    mid_points = []
    for (x1, y1), (x2, y2) in combinations(lst, 2):
        mid_points.append(((x2+x1)/2, (y2+y1)/2))
    return len(set(mid_points)) == 5

